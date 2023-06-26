import os

import boto3
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from projects.image_to_ascii_art.models import UserUploadedImage


def load():
    print('image_to_ascii_art signals loaded.')


@receiver(pre_delete, sender=UserUploadedImage)
def delete_submitted_file_from_s3(sender, instance: UserUploadedImage, **kwargs):
    s3 = boto3.client(
        's3',
        region_name=os.getenv('AWS_S3_CUSTOM_DOMAIN').split('.')[1],
        endpoint_url='https://' + os.getenv('AWS_S3_CUSTOM_DOMAIN'),
        aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_S3_SECRET_ACCESS_KEY'),
    )
    s3.delete_object(Bucket=os.getenv('AWS_STORAGE_BUCKET_NAME'), Key=instance.image.name)
