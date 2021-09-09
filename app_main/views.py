from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Profile, Recipient, Mailing


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'app_main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(id=1)
        return context
