# Generated by Django 4.2.5 on 2023-10-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_alter_photo_options_photo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
