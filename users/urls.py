from turtle import home
from django.urls import path
from .views import PasswordView
from users.views import indexview,SignUpView,home,LoginView,LogoutView
# from django.contrib.auth import views as auth_views
from .import views
app_name  = 'users'

urlpatterns = [
     path('',indexview.as_view(),name='index'),
     path('home/',home.as_view(),name='home'),
     path('signup/',SignUpView.as_view(),name = 'signup'),
     path('login/',LoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(),name='logout'),
     path('passwordchange/',PasswordView.as_view(template_name='registration/passwordchange.html'),name='passwordchange'),
     path('password_success/',views.password_success,name='password_success'),   
]