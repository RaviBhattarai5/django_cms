# Generated by Django 5.0.6 on 2024-10-07 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateCode', models.CharField(max_length=10)),
                ('stateName', models.CharField(max_length=100)),
                ('capitalName', models.CharField(max_length=100)),
                ('disable', models.BooleanField(default=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='country.country')),
            ],
        ),
    ]