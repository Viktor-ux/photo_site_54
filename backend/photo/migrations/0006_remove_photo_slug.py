# Generated by Django 4.2.5 on 2023-12-06 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_remove_photo_cat_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='slug',
        ),
    ]
