from collections.abc import Iterator

from apps.contacts.models import Contact
from apps.contacts.services import faker


def generate_user() -> Contact:
    return Contact(name=faker.unique.username(), email=faker.unique.company_email(), password=faker.unique.password())


def generate_users(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_user()
