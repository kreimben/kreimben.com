from django.core.cache import cache
from django.core.paginator import EmptyPage
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, ListView, DetailView

from .models import Post, SubmittedFile, Category
from .utils import _save_ip_and_get_file, _get_client_ip


class BlogView(ListView):
    template_name = "blog/blog.html"
    model = Post
    paginate_by = 15

    def paginate_queryset(self, queryset, page_size):
        """
        Due to paginator's limit for dealing with page number fallback,
        Hereby I re-implement the `paginate_queryset` method.
        """
        paginator = self.get_paginator(
            queryset,
            page_size,
            orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty(),
        )
        page_kwarg = self.page_kwarg
        page_num = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1

        try:
            page_num = int(page_num)
        except ValueError:
            page_num = 1

        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page_num = paginator.num_pages
            page = paginator.page(page_num)

        return paginator, page, page.object_list, page.has_other_pages()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            "categories": [cate.name for cate in Category.objects.all()],
            "selected_category_name": self.request.GET.get('category', None)
        }
        return super().get_context_data(**context)

    def get_queryset(self):
        category_name = self.request.GET.get('category', None)
        query = self.request.GET.get('q', None)

        if category_name:
            posts = Post.published.filter(category__name=category_name)
        elif query:
            posts = Post.published.filter(
                Q(content__icontains=query) |
                Q(title__icontains=query) |
                Q(subtitle__icontains=query)
            )
        else:
            posts = Post.published.all()

        return posts


class BlogPostDetailView(DetailView):
    template_name = "blog/blog_post.html"
    model = Post
    context_object_name = 'post'  # This automatically adds the Post object to the context as 'post'

    def get_object(self, queryset=None):
        # Override to use 'post_id' from kwargs and add view count logic
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(self.get_queryset(), id=post_id, status='published')

        # Increment view count if not viewed in this session
        if not cache.get(f"post_{post.id}_viewed"):
            cache.set(f"post_{post.id}_viewed", True)  # use default timeout
            post.view_count += 1
            post.save()

        return post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        post = context['post']
        # Add in the submitted files
        context['files'] = SubmittedFile.objects.filter(post=post).exists()
        # Add client IP
        context['ip'] = _get_client_ip(self.request)
        return context


class BlogFileDownloadCounterView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'file_download'

    def get_redirect_url(self, *args, **kwargs):
        f: SubmittedFile = _save_ip_and_get_file(kwargs['file_id'], kwargs['ip'])
        url = f.download
        return url
