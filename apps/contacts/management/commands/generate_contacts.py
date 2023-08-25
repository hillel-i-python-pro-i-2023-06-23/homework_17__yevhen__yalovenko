from django.core.management.base import BaseCommand

from apps.contacts.services.generate_and_save_contacts import generate_and_save_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            type=int,
            help="How many contacts do you want to generate?",
            default=12,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        generate_and_save_contacts(amount=amount)
