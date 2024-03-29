# Generated by Django 5.0 on 2024-01-05 21:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_remove_user_facebook_link_remove_user_instagram_link_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("user.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("user.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("Simple", "Simple"), ("Team", "Team"), ("Admin", "Admin")],
                max_length=20,
            ),
        ),
    ]
