# Generated by Django 5.0.6 on 2024-10-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holidays',
            old_name='createdBY',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='holidays',
            old_name='holiday_Name',
            new_name='holiday_name',
        ),
        migrations.RenameField(
            model_name='holidays',
            old_name='holidayType',
            new_name='holiday_type',
        ),
        migrations.RenameField(
            model_name='holidays',
            old_name='sessionYr',
            new_name='session_year',
        ),
        migrations.AddField(
            model_name='holidays',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]