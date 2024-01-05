# Generated by Django 5.0 on 2023-12-16 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=500)),
                ("illustration", models.CharField(max_length=20)),
            ],
            options={
                "ordering": ["-title"],
            },
        ),
        migrations.CreateModel(
            name="FeedBack",
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
                ("message", models.CharField(max_length=500)),
                ("author", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.CharField(max_length=50)),
                (
                    "author_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="FeedBack",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-message"],
            },
        ),
        migrations.CreateModel(
            name="Price",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("basic", "BASIC"),
                            ("premium", "PREMIUM"),
                            ("pro", "PRO"),
                        ],
                        max_length=50,
                    ),
                ),
                ("description", models.CharField(max_length=100)),
                ("amount", models.IntegerField()),
                ("duration", models.IntegerField()),
                ("limited", models.BooleanField(db_default=models.Value(True))),
                ("number", models.IntegerField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="price",
                        to="general.service",
                    ),
                ),
            ],
        ),
    ]
