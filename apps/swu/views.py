from django.views.generic import TemplateView

from .models import Character
from .models import SpecialLog


class HomeView(TemplateView):
    template_name = 'swu/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['family'] = Character.family.all()
        return context


class RequestView(TemplateView):
    template_name = 'swu/logs.html'

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context['requests'] = SpecialLog.objects.all()[:10]
        return context


class ExploreView(TemplateView):
    template_name = 'swu/explore.html'

    def get_context_data(self, **kwargs):
        context = super(ExploreView, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.all()
        return context
