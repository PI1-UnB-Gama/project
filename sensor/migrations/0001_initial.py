# Generated by Django 5.0.6 on 2024-06-11 02:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
        ),
    ]
