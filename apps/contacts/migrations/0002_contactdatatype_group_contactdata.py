# Generated by Django 4.2.4 on 2023-08-25 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactDataType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("regex_pattern", models.CharField(help_text="Regular expression for validation", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("contacts", models.ManyToManyField(related_name="groups", to="contacts.contact")),
            ],
        ),
        migrations.CreateModel(
            name="ContactData",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("value", models.CharField(max_length=200)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="contact_data", to="contacts.contact"
                    ),
                ),
                (
                    "data_type",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="contacts.contactdatatype"),
                ),
            ],
        ),
    ]
