# Generated by Django 5.1.1 on 2024-09-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='isRole',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
