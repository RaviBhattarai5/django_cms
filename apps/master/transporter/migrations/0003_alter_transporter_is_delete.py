# Generated by Django 5.0.6 on 2024-10-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporter', '0002_alter_transporter_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporter',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]