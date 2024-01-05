# Generated by Django 5.0 on 2023-12-27 17:41

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_user_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="facebook_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="instagram_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="linkedIn_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name=django.db.models.expressions.CombinedExpression(
                    models.F("username"), "+", models.Value("_pic")
                ),
            ),
        ),
    ]
