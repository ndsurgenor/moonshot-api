# Generated by Django 3.2.4 on 2024-02-13 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='value',
        ),
    ]
