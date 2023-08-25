import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--delete-by-pk",
            type=int,
            help="Delete by primary key",
        )
        parser.add_argument(
            "--delete-by-date",
            type=str,
            help="Delete by date (format: YYYY-MM-DD)",
        )

    def handle(self, *args, **options):
        delete_by_pk: int = options["delete_by_pk"]
        delete_by_date: int = options["delete_by_date"]

        logger = logging.getLogger("django")

        queryset = Contact.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        if delete_by_date:
            queryset_for_delete = Contact.objects.filter(created_at__date=delete_by_date)
        elif delete_by_pk:
            queryset_for_delete = Contact.objects.filter(id=delete_by_pk)
        else:
            queryset_for_delete = queryset

        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of contacts after: {queryset.count()}")
