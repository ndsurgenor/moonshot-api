# Generated by Django 3.2.4 on 2024-02-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20240131_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='main_feature',
            field=models.CharField(choices=[('aurora', 'Aurora'), ('deep_sky', 'Deep-Sky'), ('moon', 'Moon'), ('nightscape', 'Nightscape'), ('planet', 'Planet'), ('stars', 'Stars'), ('other', '(Other)')], max_length=127),
        ),
    ]
