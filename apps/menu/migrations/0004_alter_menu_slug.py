# Generated by Django 5.1.1 on 2024-09-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]