import os

import boto3
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver

from blog.models import Category, Post, SubmittedFile


def load():
    print('blog signals loaded.')


@receiver(post_save, sender=Category)
def clear_cache_category_post_save(sender: Category, **kwargs):
    cache.delete('categories')


@receiver(post_delete, sender=Category)
def clear_cache_category_post_delete(sender: Category, **kwargs):
    cache.delete('categories')
    # After `Category` model deleted and related `Post` model deleted, Django doesn't call `post_delete` on signal.
    cache.delete('posts')


@receiver(post_save, sender=Post)
def clear_cache_post_post_save(sender: Post, **kwargs):
    cache.delete('posts')


@receiver(post_delete, sender=Post)
def clear_cache_post_post_delete(sender: Post, **kwargs):
    cache.delete('posts')


@receiver(pre_delete, sender=SubmittedFile)
def delete_submitted_file_from_s3(sender, instance: SubmittedFile, **kwargs):
    s3 = boto3.client(
        's3',
        region_name=os.getenv('AWS_S3_CUSTOM_DOMAIN').split('.')[1],
        endpoint_url='https://' + os.getenv('AWS_S3_CUSTOM_DOMAIN'),
        aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_S3_SECRET_ACCESS_KEY'),
    )
    s3.delete_object(Bucket=os.getenv('AWS_STORAGE_BUCKET_NAME'), Key=instance.file.name)
