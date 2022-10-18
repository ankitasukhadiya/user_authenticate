from urllib import request
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import TemplateView,CreateView,View
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import PasswordChangeView
from users.forms import SignUpForm
from django.contrib.auth import get_user_model
from User_Authenticate.settings import LOGOUT_REDIRECT_URL,AUTH_USER_MODEL
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect,redirect
from .forms import AuthenticationForm, PasswordChangingForm
from django.contrib import messages

user = AUTH_USER_MODEL
User = get_user_model()

class indexview(TemplateView):
    template_name = 'index.html'

class home(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    
    def form_valid(self,form):
        success_url = super().form_valid(form)
        self.object = form.save()
        form.save()  
        return success_url 
     
class LoginView(BaseLoginView):
    print("helooooo")
    template_name = 'registration/login.html' 
    form_class = AuthenticationForm
    print("-=-==-=-1=--===-")
    # print(request.method,"-=-==-=-1=--===-")
    def form_valid(self,form):
        print(self.request.method,"-=-==-=-1=--===-")
        user = form.get_user()
        self.request.session["pk"] = user.pk
        print(user,"-=-=-=-=-=-=-=")
        return HttpResponseRedirect(reverse_lazy("users:home"))
   
class LogoutView(View):
    print("-=-=-=-=-=-1logot56925692569256925")
    def get(self, request):
        print("=-==-=-=-8---")
        logout(request)
        return redirect(LOGOUT_REDIRECT_URL)    

class PasswordChange(PasswordChangeView):
    template_name = 'registration/change-password.html'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('users:password_success')

def password_success(request):
    return render(request,"registration/password_success.html",{})

  

