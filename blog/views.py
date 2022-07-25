from django.views.generic import TemplateView, DetailView
from .models import Post


class BlogView(TemplateView):
    template_name = '../templates/blog/blog.html'

    def get(self, request, **kwargs):
        posts = Post.objects.order_by('-created_at').all()
        context = {
            'posts': posts
        }
        return self.render_to_response(context)


class BlogPostDetailView(DetailView):
    template_name = '../templates/blog/blog_post.html'
    model = Post

    def get(self, request, **kwargs):
        post = Post.objects.filter(id=kwargs['post_id']).first()
        print(post.categories.name)
        context = {
            'post': post
        }
        return self.render_to_response(context)
