# Generated by Django 4.2.1 on 2023-05-12 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_to_ascii_art', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useruploadedimage',
            options={'get_latest_by': ['-updated_at'], 'verbose_name': 'User Uploaded Image', 'verbose_name_plural': 'User Uploaded Images'},
        ),
    ]
