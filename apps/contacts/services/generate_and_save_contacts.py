import random

from apps.contacts.models import Contact
from apps.contacts.models.contact import ContactData
from apps.contacts.models.group import Group

from apps.contacts.services import data_types, data_type_generators
from apps.contacts.services.faker_init import faker


def generate_and_save_contacts(amount: int):
    possible_groups = ["family", "friends", "work", "gamers"]
    for _ in range(amount):
        random_choice = random.randint(0, 3)
        contact = Contact.objects.create(name=faker.unique.first_name(), birthday=faker.date_of_birth())
        group = Group.objects.get_or_create(name=possible_groups[random_choice])[0]
        contact.groups.add(group)

        for data_type in data_types:
            if data_type.name in data_type_generators:
                generator = data_type_generators[data_type.name]
                ContactData.objects.get_or_create(contact=contact, data_type=data_type, defaults={"value": generator()})
