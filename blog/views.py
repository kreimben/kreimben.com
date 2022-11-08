from urllib.request import urlopen

import ujson
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, RedirectView

from .models import Category, Post, SubmittedFile, Downloader


class BlogView(TemplateView):
    template_name = "../templates/blog/blog.html"

    def get(self, request: HttpRequest, **kwargs):
        posts = ""
        category = request.GET.get("category")
        if category is not None:
            posts = (Post.objects.order_by("-created_at").filter(
                Q(category__name=category) & Q(status="published")).all())
        else:
            posts = (Post.objects.order_by("-created_at").filter(
                status="published").all())
        page = Paginator(posts, 15)

        categories = Category.objects.order_by("name").all()

        page_number = request.GET.get("page")
        page_obj = page.get_page(page_number)

        context = {"page_obj": page_obj, "categories": categories}
        return self.render_to_response(context)


class BlogPostDetailView(DetailView):
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
        print(f'files: {files}')
        context = {"post": post, 'files': files, 'ip': self._get_client_ip(request)}
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

        file = get_object_or_404(SubmittedFile, id=file_id)

        if info['status'] == 'fail':
            d = Downloader(
                file=file,
                ip_address=ip_address
            )
        else:
            d = Downloader(
                file=file,
                ip_address=ip_address,
                city=info['city'],
                country_name=info['country'],
                latitude=info['lat'],
                longitude=info['lon'],
                time_zone=info['timezone'],
            )

        d.save()

        return d

    def get_redirect_url(self, *args, **kwargs):
        self._extract_downloader_info(kwargs['file_id'], kwargs['ip'])
        file: SubmittedFile = get_object_or_404(SubmittedFile, id=kwargs['file_id'])
        url = file.download
        return url


class PostSearchView(ListView):
    template_name = "blog/blog.html"
    model = Post
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = (Post.objects.order_by("-created_at").filter(
            Q(content__icontains=query)
            | Q(title__icontains=query)
            | Q(subtitle__icontains=query)).filter(status="Published"))
        return object_list
