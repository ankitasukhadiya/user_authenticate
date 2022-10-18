from turtle import home
from django.urls import path
from .views import PasswordChange
from users.views import indexview,SignUpView,home,LoginView,LogoutView
from django.contrib.auth import views as auth_views
from .import views
app_name  = 'users'

urlpatterns = [
     path('',indexview.as_view(),name='index'),
     path('home/',home.as_view(),name='home'),
     path('signup/',SignUpView.as_view(),name = 'signup'),
     path('login/',LoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(),name='logout'),
     path('change-password/',PasswordChange.as_view(template_name='registration/change-password.html'),name='change-password'),
     path('password_success/',views.password_success,name='password_success'),

     
]