from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from .models import Post


class BlogView(TemplateView):
    template_name = '../templates/blog/blog.html'

    def get(self, request: HttpRequest, **kwargs):
        posts = Post.objects.order_by('-created_at').all()
        page = Paginator(posts, 15)

        page_number = request.GET.get('page')
        page_obj = page.get_page(page_number)

        if page_number is None or page_number != str(page_obj.number):
            return HttpResponseRedirect('?page=1')

        context = {
            'page_obj': page_obj
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
