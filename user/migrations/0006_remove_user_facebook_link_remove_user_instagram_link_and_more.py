# Generated by Django 5.0 on 2024-01-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_facebook_link_user_instagram_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='user',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='user',
            name='linkedIn_link',
        ),
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='twitter_link',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Simple', 'Simple'), ('Team', 'Team'), ('Core', 'Core'), ('Admin', 'Admin')], default='', max_length=20),
            preserve_default=False,
        ),
    ]