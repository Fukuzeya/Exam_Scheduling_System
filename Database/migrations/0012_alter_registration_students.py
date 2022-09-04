# Generated by Django 3.2 on 2022-07-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0011_session1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='registered_students', to='Database.Student'),
        ),
    ]