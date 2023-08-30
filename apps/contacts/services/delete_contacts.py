from apps.contacts.models import Contact


def delete_contacts():
    return Contact.objects.all().delete()
