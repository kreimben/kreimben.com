from home.views import BaseTemplateView
from projects.sort_visualizer.models import Sort


class SortVisualizerView(BaseTemplateView):
    template_name = 'sort_visualizer/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sort Visualizer'
        context['sorting'] = Sort.objects.all()
        return context
