# Generated by Django 4.2.1 on 2023-06-13 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traceback', models.TextField()),
                ('status_code', models.IntegerField()),
                ('path', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=255)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
