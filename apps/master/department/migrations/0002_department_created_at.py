# Generated by Django 5.1.1 on 2024-10-07 04:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]