# Generated by Django 4.1.2 on 2022-10-23 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0002_tour_beginning_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='tour_id',
            new_name='tour',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='tourist_id',
        ),
    ]