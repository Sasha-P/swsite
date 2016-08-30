from django.views.generic import TemplateView

from .models import Character


class HomeView(TemplateView):
    template_name = 'swu/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['family'] = Character.family.all()
        return context
