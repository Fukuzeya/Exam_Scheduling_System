# Generated by Django 3.2 on 2022-07-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scheduling', '0013_alter_invigilatorassignment_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='has_assigned',
            field=models.BooleanField(default=False),
        ),
    ]