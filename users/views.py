from urllib import request
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.urls import reverse_lazy
from .forms import ChangePasswordForm
from django.views.generic import TemplateView,CreateView,View
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import PasswordChangeView
from users.forms import SignUpForm
from django.contrib.auth import get_user_model
from User_Authenticate.settings import AUTH_USER_MODEL
from django.contrib.auth import authenticate
from django.contrib.auth import logout as Django_logout
from django.shortcuts import HttpResponseRedirect,redirect
from .forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash
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
    success_url = reverse_lazy('users:home')

    def form_valid(self,form):
        success_url = super().form_valid(form)
        user = form.get_user()
        self.request.session["pk"] = user.id
        user.save()
        print(user,"-=-=-=-user  1=-=-=-=")
        return success_url

class LogoutView(View):
    def get(self, request):  
        Django_logout(request)
        return HttpResponseRedirect(reverse_lazy("users:login"))   

class ChangePasswordView(PasswordChangeView):
    print("hellooooo")
    template_name = "registration/change_password.html"
    form_class = ChangePasswordForm
    # success_url = reverse_lazy('users:password_success')

    def form_valid(self, form):    
        old_password = self.request.POST["old_password"]
        new_password1 = self.request.POST["new_password1"]
        if old_password == new_password1:
            return redirect(reverse_lazy("change_password"))
        update_session_auth_hash(self.request, form.user)
        form.save()
        return HttpResponseRedirect(reverse_lazy("users:password_success"))

class password_success(TemplateView):
    template_name = "registration/password_success.html"
      



   



  

