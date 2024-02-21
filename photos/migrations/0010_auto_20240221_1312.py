# Generated by Django 3.2.4 on 2024-02-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20240220_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='main_feature',
            field=models.CharField(choices=[('aurora', 'Aurora'), ('deep-sky', 'Deep-Sky'), ('moon', 'Moon'), ('nightscape', 'Nightscape'), ('planet', 'Planet'), ('stars', 'Stars'), ('other', '(Other)')], max_length=127),
        ),
        migrations.AlterField(
            model_name='photo',
            name='other_equipment_used',
            field=models.TextField(blank=True, null=True),
        ),
    ]
