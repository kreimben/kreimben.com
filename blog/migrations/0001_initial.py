# Generated by Django 4.0.6 on 2022-07-26 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, unique=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "get_latest_by": "-created_at",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, unique=True)),
                ("subtitle", models.CharField(max_length=200, null=True)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "post",
                "verbose_name_plural": "posts",
                "get_latest_by": ["title", "-created_at"],
            },
        ),
    ]
