# Generated by Django 5.1.1 on 2024-11-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                ("dist", models.IntegerField(default=0)),
                ("desc", models.CharField(max_length=1000)),
            ],
        ),
    ]
