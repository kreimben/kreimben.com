from urllib.request import urlopen

import ujson
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, RedirectView

from home.views import BaseTemplateView, BaseDetailView
from .models import Post, SubmittedFile, Downloader


class BlogView(BaseTemplateView):
    template_name = "../templates/blog/blog.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        category_name = request.GET.get('category', None)
        context = self.get_context_data()

        if category_name is None:
            posts = Post.published.all()
        else:
            posts = Post.published.filter(category__name=category_name)

        categories = set(list(post.category.name for post in posts))

        page = Paginator(posts, 15)

        page_number = request.GET.get('page', 1)
        page_obj = page.get_page(page_number)

        context["page_obj"] = page_obj
        context["categories"] = categories
        return self.render_to_response(context)


class BlogPostDetailView(BaseDetailView):
    template_name = "../templates/blog/blog_post.html"
    model = Post

    def _get_client_ip(self, request: HttpRequest):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get(self, request, **kwargs):
        post = get_object_or_404(Post, Q(id=kwargs["post_id"]) & Q(status='published'))
        try:
            files = SubmittedFile.objects.filter(post=post)
        except SubmittedFile.DoesNotExist:
            files = None

        if not cache.get(f'{post.id}/{self._get_client_ip(request)}'):
            post.view_count += 1
            post.save()
            cache.set(f'{post.id}/{self._get_client_ip(request)}', True, 30 * 60)

        context = self.get_context_data()
        context['post'] = post
        context['files'] = files
        context['ip'] = self._get_client_ip(request)
        return self.render_to_response(context)


class BlogFileDownloadCounterView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'file_download'

    def _get_geo_info(self, ip):
        response = urlopen("http://ip-api.com/json/" + ip).read().decode('utf-8')
        return ujson.loads(response)

    def _extract_downloader_info(self, file_id, ip_address) -> Downloader:
        info = self._get_geo_info(ip_address)

        f = get_object_or_404(SubmittedFile, id=file_id)

        if info['status'] == 'fail':
            d = Downloader(
                file=f,
                ip_address=ip_address
            )
        else:
            d = Downloader(
                file=f,
                ip_address=ip_address,
                city=info['city'],
                country_name=info['country'],
                latitude=info['lat'],
                longitude=info['lon'],
                time_zone=info['timezone'],
            )

        d.save()

        return d

    async def get_redirect_url(self, *args, **kwargs):
        self._extract_downloader_info(kwargs['file_id'], kwargs['ip'])
        f: SubmittedFile = get_object_or_404(SubmittedFile, id=kwargs['file_id'])
        url = f.download
        return url


class PostSearchView(ListView):
    template_name = "blog/blog.html"
    model = Post
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = (Post.published.filter(
            Q(content__icontains=query)
            | Q(title__icontains=query)
            | Q(subtitle__icontains=query)))
        return object_list
