from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, RedirectView

from home.views import BaseTemplateView, BaseDetailView
from .models import Post, SubmittedFile, Downloader

class BlogView(ListView):
    template_name = "blog/blog.html"
    model = Post
    paginate_by = 15

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
        context["selected_category_name"] = category_name
        return self.render_to_response(context)


def _get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class BlogPostDetailView(BaseDetailView):
    template_name = "../templates/blog/blog_post.html"
    model = Post

    def get(self, request, **kwargs):
        post = get_object_or_404(Post, Q(id=kwargs["post_id"]) & Q(status='published'))
        try:
            files = SubmittedFile.objects.filter(post=post)
        except SubmittedFile.DoesNotExist:
            files = None

        if not cache.get(f"post_{post.id}_viewed"):
            cache.set(f"post_{post.id}_viewed", True)  # use default timeout
            post.view_count += 1
            post.save()

        context = self.get_context_data()
        context['post'] = post
        context['files'] = files
        context['ip'] = _get_client_ip(request)
        return self.render_to_response(context)


def _save_ip_and_get_file(file_id, ip_address):
    f = get_object_or_404(SubmittedFile, id=file_id)

    d = Downloader.objects.create(
        file=f,
        ip_address=ip_address
    )

    return f


class BlogFileDownloadCounterView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'file_download'

    def get_redirect_url(self, *args, **kwargs):
        f: SubmittedFile = _save_ip_and_get_file(kwargs['file_id'], kwargs['ip'])
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
