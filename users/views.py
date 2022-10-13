from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from users.forms import SignUpForm

class indexview(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

  

