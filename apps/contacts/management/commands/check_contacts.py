from django.core.management.base import BaseCommand

from apps.contacts.models import Contact


class Command(BaseCommand):
    help = "Check if there are any contacts in the database"

    def handle(self, *args, **options):
        if Contact.objects.exists():
            self.stdout.write("True")
        else:
            self.stdout.write("False")
