# Generated by Django 5.0 on 2024-01-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0008_user_facebook_link_user_instagram_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="users"),
        ),
    ]