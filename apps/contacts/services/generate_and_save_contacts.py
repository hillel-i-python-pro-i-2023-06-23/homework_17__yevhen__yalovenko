import random

from apps.contacts.models import Contact
from apps.contacts.models.contact import ContactData
from apps.contacts.models.group import Group

from apps.contacts.services.data_types import create_data_types
from apps.contacts.services.faker_init import faker


def generate_and_save_contacts(amount: int):
    possible_groups = ["family", "friends", "work", "gamers"]
    data_types, data_type_generators = create_data_types()
    for _ in range(amount):
        random_choice = random.randint(0, 3)
        contact = Contact.objects.create(name=faker.unique.first_name(), birthday=faker.date_of_birth())
        group, _ = Group.objects.get_or_create(name=possible_groups[random_choice])
        contact.groups.add(group)

        # Generate a random number of data types for each contact
        num_data_types = random.randint(1, len(data_types))
        # Shuffle the data types list and take the first num_data_types elements
        random.shuffle(data_types)
        selected_data_types = data_types[:num_data_types]

        for data_type in selected_data_types:
            if data_type.name in data_type_generators:
                generator = data_type_generators[data_type.name]
                ContactData.objects.get_or_create(contact=contact, data_type=data_type, defaults={"value": generator()})
