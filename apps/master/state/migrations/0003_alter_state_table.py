# Generated by Django 5.1.2 on 2024-10-09 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0002_rename_capitalname_state_capital_name_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='state',
            table='master_state',
        ),
    ]