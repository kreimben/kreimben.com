# Generated by Django 4.2.1 on 2023-05-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_to_ascii_art', '0005_rename_compress_ratio_imageconvertingresult_compress_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageconvertingresult',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
