# Generated by Django 5.1.1 on 2024-09-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menu_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]