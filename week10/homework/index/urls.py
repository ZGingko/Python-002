from django.urls import path
from . import views

urlpatterns = [
    path('', views.mylogin),
    path('login', views.mylogin)
]