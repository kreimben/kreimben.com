# Generated by Django 4.1.1 on 2022-09-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0008_alter_post_status_submittedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedfile',
            name='download_count',
            field=models.IntegerField(default=0),
        ),
    ]
