from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'


class Privacidade(TemplateView):
    template_name = 'privacidade.html'



