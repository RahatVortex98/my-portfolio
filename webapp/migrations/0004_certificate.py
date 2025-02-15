# Generated by Django 5.1.6 on 2025-02-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0003_project_alter_configuration_facebook_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Course Name")),
                (
                    "image_certificate",
                    models.ImageField(
                        upload_to="certificates/", verbose_name="Course Certificate"
                    ),
                ),
            ],
        ),
    ]
