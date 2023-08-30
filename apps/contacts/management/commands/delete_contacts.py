from django.core.management.base import BaseCommand

from apps.contacts.services.delete_contacts import delete_contacts


class Command(BaseCommand):
    def handle(self, *args, **options):
        delete_contacts()
