# Generated by Django 4.2.1 on 2023-05-12 08:43

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedfile',
            name='file',
            field=models.FileField(upload_to=blog.models.submitted_file_path),
        ),
    ]
