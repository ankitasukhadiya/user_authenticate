from django.urls import path
# from .import views
from users.views import indexview,SignUpView

urlpatterns = [
     path('',indexview.as_view(),name='index'),
     path('signup/',SignUpView.as_view(),name = "signup"),
]