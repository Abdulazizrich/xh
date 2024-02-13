# Generated by Django 5.0.1 on 2024-02-06 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Togri_soz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Notogri_soz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=255)),
                ('togrisoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.togri_soz')),
            ],
        ),
    ]
