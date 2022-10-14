from turtle import home
from django.urls import path
from .import views
from users.views import indexview,SignUpView,home,LoginView,base
app_name  = 'users'

urlpatterns = [
     path('',indexview.as_view(),name='index'),
     path('signup/',SignUpView.as_view(),name = 'signup'),
     path('home/',home.as_view(),name='home'),
     path('login/',LoginView.as_view(),name='login'),
     path('base/',base.as_view(),name='base'),

    
]