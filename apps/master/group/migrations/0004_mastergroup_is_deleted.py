# Generated by Django 5.0.6 on 2024-10-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_rename_categoryid_mastergroup_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastergroup',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]