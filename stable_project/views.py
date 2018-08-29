from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from results.models import Events
from django.utils import timezone

class Home(TemplateView):
    template_name = "index.html"

class Portfolio(TemplateView):
    template_name = "portfolio.html"


class DynamicURL(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        print('hello')
        print(kwargs)
        #ADD {{things}} to index.html to test that it works - go to url /r/lskdjfalksdthings and it should show up
        return kwargs
