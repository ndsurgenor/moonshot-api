# Generated by Django 3.2.4 on 2024-02-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_auto_20240221_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='camera_used',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='lens_used',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='photo',
            name='other_equipment_used',
            field=models.TextField(blank=True),
        ),
    ]
