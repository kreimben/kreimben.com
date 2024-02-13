from django.http import HttpRequest
from django.views.generic import TemplateView

from blog.models import Post


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request: HttpRequest, **kwargs):
        context = self.get_context_data(**kwargs)
        context['head_posts'] = list(Post.published.all().order_by('-created_at'))[:3]
        return self.render_to_response(context)
