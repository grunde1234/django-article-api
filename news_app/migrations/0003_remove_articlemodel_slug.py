# Generated by Django 5.2.2 on 2025-06-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_alter_articlemodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='slug',
        ),
    ]
