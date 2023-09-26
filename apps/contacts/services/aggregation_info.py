from datetime import date
from typing import NamedTuple

from django.db import models
from django.db.models import ExpressionWrapper, FloatField, F

from apps.contacts.models import ContactDataType, Contact


def calculate_age(birthdate):
    today = date.today()
    if birthdate:
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age == 0:
            age = today - birthdate
            return f"{age.days} days"
        return f"{age} years"
    return None


class ContactInfo(NamedTuple):
    youngest_age: str = None
    youngest_birthdate: date = None
    oldest_age: str = None
    oldest_birthdate: date = None


def show_contact_info() -> ContactInfo:
    contact_info = Contact.objects.aggregate(youngest=models.Max("birthday"), oldest=models.Min("birthday"))

    if contact_info:
        youngest_birthdate = contact_info.get("youngest")
        oldest_birthdate = contact_info.get("oldest")

        youngest_age = calculate_age(youngest_birthdate)
        oldest_age = calculate_age(oldest_birthdate)

        return ContactInfo(
            youngest_age=youngest_age,
            youngest_birthdate=youngest_birthdate,
            oldest_age=oldest_age,
            oldest_birthdate=oldest_birthdate,
        )

    return ContactInfo()


def show_average_age():
    query_set = Contact.objects.all()
    if query_set:
        average_age = query_set.aggregate(
            average_age=models.Avg(ExpressionWrapper(F("birthday"), output_field=FloatField()))
        )
        age = average_age["average_age"]
        average = calculate_age(date(year=int(age), month=1, day=1))
        return average


def show_contact_data_types_counts():
    contact_data_types_counts = ContactDataType.objects.annotate(count=models.Count("contactdata__contact")).values(
        "name", "count"
    )

    return contact_data_types_counts


def show_contacts_data_count():
    contacts_with_data_counts = Contact.objects.annotate(
        data_count=models.Count("contact_data__data_type", distinct=True)
    )
    return contacts_with_data_counts
