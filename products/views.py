from django.http import HttpRequest
from django.views.generic import DetailView


class ProductsView(DetailView):
    template_name = 'products/products.html'

    def get(self, request: HttpRequest, **kwargs):
        context = {

        }
        return self.render_to_response(context)
