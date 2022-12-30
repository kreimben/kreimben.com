from django.views.generic import TemplateView


class ChatView(TemplateView):
    template_name = '../templates/chat/chat.html'
