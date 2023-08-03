# Generated by Django 4.2.4 on 2023-08-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_squashed_0005_alter_contact_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-modified_at", "name"],
            },
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
    ]
