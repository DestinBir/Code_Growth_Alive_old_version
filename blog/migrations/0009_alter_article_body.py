# Generated by Django 5.0.2 on 2024-02-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_rename_article_article_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="body",
            field=models.TextField(),
        ),
    ]