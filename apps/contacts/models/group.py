from django.db import models

from apps.contacts.models import Contact


class Group(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ManyToManyField(Contact, related_name="groups")

    def __str__(self):
        return self.name
