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
from User_Authenticate.settings import AUTH_USER_MODEL
from django.contrib.auth import authenticate
from django.contrib.auth import logout as Django_logout
from django.shortcuts import HttpResponseRedirect,redirect
from .forms import AuthenticationForm, PasswordChangingForm,p

user = AUTH_USER_MODEL
User = get_user_model()

class indexview(TemplateView):
    template_name = 'index.html'
   
class home(TemplateView): 
    template_name = 'home.html'
    def get_context_data(self):
        user_id = self.request.session['pk']
        user = User.objects.filter(id = user_id).get()
        print("-=-=-=user- 2 =-=-",user)  
        context = {
            'user':user,
        }
        return context
        
class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    success_message = "Your signup was created successfully"
    
    def form_valid(self,form):
        success_url = super().form_valid(form)
        self.object = form.save()
        form.save() 
        print(form,"-=-=-=-=form----") 
        return success_url 
     
class LoginView(BaseLoginView):
    template_name = 'registration/login.html' 
    form_class = AuthenticationForm
    def form_valid(self,form):
        user = form.get_user()
        self.request.session["pk"] = user.id
        user.save()
        print(user,"-=-=-=-user  1=-=-=-=")
        return HttpResponseRedirect(reverse_lazy("users:home"))

class LogoutView(View):
    def get(self, request):  
        Django_logout(request)
        return HttpResponseRedirect(reverse_lazy("users:login"))   

class PasswordView(PasswordChangeView):
    print("heloooooo 888888888")
    template_name = 'registration/passwordchange.html'
    form_class = PasswordChangingForm   
    success_url = reverse_lazy('users:password_success')     

def password_success(request):
    return render(request,"registration/password_success.html",{})    



   



  

