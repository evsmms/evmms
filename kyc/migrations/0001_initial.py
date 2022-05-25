# Generated by Django 3.2.5 on 2022-05-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30, verbose_name='vehicle_model')),
                ('plate_number', models.CharField(max_length=30, verbose_name='Plate number')),
                ('category', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30, verbose_name='Operation status')),
            ],
        ),
    ]
