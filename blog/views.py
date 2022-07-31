from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest
from django.views.generic import TemplateView, DetailView

from .models import Post, Category


class BlogView(TemplateView):
    template_name = '../templates/blog/blog.html'

    def get(self, request: HttpRequest, **kwargs):
        posts = ''
        category = request.GET.get('category')
        if category is not None:
            posts = Post.objects.order_by('-created_at') \
                .filter(Q(category__name=category) & Q(status='published')) \
                .all()
            print(f'posts: {posts}')
        else:
            posts = Post.objects.order_by('-created_at').filter(status='published').all()
        page = Paginator(posts, 15)

        categories = Category.objects.order_by('name').all()

        page_number = request.GET.get('page')
        page_obj = page.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'categories': categories
        }
        return self.render_to_response(context)


class BlogPostDetailView(DetailView):
    template_name = '../templates/blog/blog_post.html'
    model = Post

    def get(self, request, **kwargs):
        post = Post.objects.filter(id=kwargs['post_id']).first()
        context = {
            'post': post
        }
        return self.render_to_response(context)
