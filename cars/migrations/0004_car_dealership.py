# Generated by Django 4.1.7 on 2023-03-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0001_initial'),
        ('cars', '0003_alter_car_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dealerships.dealership'),
        ),
    ]
