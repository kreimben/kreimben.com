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


def index(request):
    return HttpResponse('Hi, It\'s Kreimben\'s Blog.')