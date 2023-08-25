import logging

from apps.contacts.models import Contact
from apps.contacts.services.generate_users import generate_users


def generate_and_save_user(amount: int):
    logger = logging.getLogger("django")

    queryset = Contact.objects.all()

    logger.info(f"Current amount of contacts before: {queryset.count()}")

    for user in generate_users(amount=amount):
        user.save()

    logger.info(f"Current amount of contacts after: {queryset.count()}")
