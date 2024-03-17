from django.views.generic import RedirectView


class YourModelDetailView(RedirectView):
    url = 'https://mnistclassifier-6r3ghybglf6uqfbma2isax.streamlit.app'
