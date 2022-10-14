from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,View
from users.forms import SignUpForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect

user = settings.AUTH_USER_MODEL

User = get_user_model()

class indexview(TemplateView):
    template_name = 'index.html'

class home(TemplateView):
    template_name = 'home.html'

class base(TemplateView):
    template_name = 'base.html'    

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name = 'signup.html'
    success_message = "Your profile was created successfully"

class LoginView(View):
    template_name = 'login.html'
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = 'Login success!'
            return HttpResponseRedirect('/home')
        else:
            message = 'Login failed!'
            return HttpResponseRedirect('/login')
        # return render(request, self.template_name, context={'form': form, 'message': message}) 

  

