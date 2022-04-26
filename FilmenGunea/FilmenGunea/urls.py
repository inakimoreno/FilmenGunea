"""
Definition of urls for FilmenGunea.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('bozkatu/', views.bozkatu, name='bozkatu'),
    path('zaleak/', views.zaleak, name='zaleak'),
    path('login/',views.login, name='login'),
    path('register/', views.register, name='register'),
    path('menua/',views.menua, name='menua'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]
