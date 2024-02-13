from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from blog.models import SubmittedFile, Downloader


def _save_ip_and_get_file(file_id, ip_address):
    f = get_object_or_404(SubmittedFile, id=file_id)

    d = Downloader.objects.create(
        file=f,
        ip_address=ip_address
    )

    return f


def _get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
