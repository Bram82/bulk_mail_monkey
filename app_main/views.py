from django.shortcuts import render
from django.views import generic

from django.conf import settings


# Create your views here.
class IndexView(generic.TemplateView):
    print(settings.BASE_DIR)
    template_name = 'app_main/index.html'
