from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__

    class Meta:
        ordering = ["-modified_at", "name"]


class ContactDataType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    regex_pattern = models.CharField(max_length=200, help_text="Regular expression for validation")
    message = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__


class ContactData(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact_data")
    data_type = models.ForeignKey(ContactDataType, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)

    class Meta:
        unique_together = ("contact", "data_type")

    def __str__(self):
        return f"{self.contact} - {self.data_type}: {self.value}"
