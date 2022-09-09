from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, RedirectView

from .models import Category, Post, SubmittedFile


class BlogView(TemplateView):
    template_name = "../templates/blog/blog.html"

    def get(self, request: HttpRequest, **kwargs):
        posts = ""
        category = request.GET.get("category")
        if category is not None:
            posts = (Post.objects.order_by("-created_at").filter(
                Q(category__name=category) & Q(status="published")).all())
            print(f"posts: {posts}")
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

    def get(self, request, **kwargs):
        post = Post.objects.get(id=kwargs["post_id"])
        try:
            files = SubmittedFile.objects.filter(post=post)
        except SubmittedFile.DoesNotExist:
            files = None
        context = {"post": post, 'files': files}
        return self.render_to_response(context)


class BlogFileDownloadCounterView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'file_download'

    def get_redirect_url(self, *args, **kwargs):
        file: SubmittedFile = get_object_or_404(SubmittedFile, file=kwargs['file_name'])
        print(f'file: {file}')
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
        print(object_list)
        return object_list
