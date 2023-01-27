# Generated by Django 4.1.5 on 2023-01-26 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('birthday_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('owner_car_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hold_cars', related_query_name='hold_car', to='project.car')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hold_owners', related_query_name='hold_owner', to='project.owner')),
            ],
        ),
        migrations.CreateModel(
            name='DrivingLicense',
            fields=[
                ('license_id', models.IntegerField(primary_key=True, serialize=False)),
                ('license_number', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('date_of_issue', models.DateField(blank=True)),
                ('owner_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='license_owner_guy', related_query_name='license_owner', to='project.owner')),
            ],
        ),
    ]
