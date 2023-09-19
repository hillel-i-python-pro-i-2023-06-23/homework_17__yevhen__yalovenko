from collections import namedtuple
from datetime import date

from django.db import models
from django.db.models import ExpressionWrapper, FloatField, F

from apps.contacts.models import ContactDataType, Contact

ContactInfo = namedtuple("ContactInfo", ["contact", "age"])


def calculate_age(birthdate):
    today = date.today()
    if birthdate:
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age == 0:
            age = today - birthdate
            return f"{age.days} days"
        return f"{age} years"
    return None


def show_contact_data_types_counts():
    contact_data_types_counts = ContactDataType.objects.aggregate(count=models.Count("name"))
    count = contact_data_types_counts["count"]
    return f"Current amount of contact data types: {count}"


def show_contacts_data_count():
    contacts_with_data_counts = Contact.objects.annotate(
        data_count=models.Count("contact_data__data_type", distinct=True)
    )
    return contacts_with_data_counts


def show_youngest_contact():
    youngest_contact = Contact.objects.aggregate(youngest=models.Max("birthday"))
    if youngest_contact:
        youngest = youngest_contact["youngest"]
        age = calculate_age(youngest)
        return ContactInfo(contact=youngest, age=age)


def show_oldest_contact():
    oldest_contact = Contact.objects.aggregate(oldest=models.Min("birthday"))
    if oldest_contact:
        oldest = oldest_contact["oldest"]
        age = calculate_age(oldest)
        return ContactInfo(contact=oldest, age=age)


def show_average_age():
    query_set = Contact.objects.all()
    if query_set:
        average_age = query_set.aggregate(
            average_age=models.Avg(ExpressionWrapper(F("birthday"), output_field=FloatField()))
        )
        age = average_age["average_age"]
        average = calculate_age(date(year=int(age), month=1, day=1))
        return average
