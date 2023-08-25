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
