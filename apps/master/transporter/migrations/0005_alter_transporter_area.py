# Generated by Django 5.0.6 on 2024-10-22 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
        ('transporter', '0004_alter_transporter_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporter',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='area.area'),
        ),
    ]