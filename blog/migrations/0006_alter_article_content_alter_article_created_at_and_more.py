# Generated by Django 5.0.2 on 2024-02-13 11:53

import mdeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_article_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=mdeditor.fields.MDTextField(verbose_name="content"),
        ),
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
        ),
        migrations.AlterField(
            model_name="article",
            name="language",
            field=models.CharField(
                choices=[("Fr", "Fr"), ("En", "En")],
                max_length=20,
                verbose_name="language",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(blank=True, null=True, verbose_name="slug"),
        ),
        migrations.AlterField(
            model_name="article",
            name="tag",
            field=models.CharField(max_length=500, verbose_name="tag"),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=255, verbose_name="title"),
        ),
    ]
