from turtle import home
from django.urls import path
from .views import ChangePasswordView
from users.views import indexview,SignUpView,home,LoginView,LogoutView,password_success,ImageView
# from django.contrib.auth import views as auth_views
from .import views
app_name  = 'users'

urlpatterns = [   
     path('',indexview.as_view(),name='index'),
     path('home/',home.as_view(),name='home'),
     path('signup/',SignUpView.as_view(),name = 'signup'),
     path('login/',LoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(),name='logout'),   
     path('change_password/',ChangePasswordView.as_view(template_name="registration/change_password.html"),name='change_password'),
     path('password_success/',password_success.as_view(),name='password_success'), 
     path('image/',ImageView.as_view(),name='image'),


]