# Generated by Django 4.1.1 on 2022-09-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0009_submittedfile_download_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedfile',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
