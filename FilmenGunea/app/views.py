"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Filma
from . import forms

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/menua.html',
        {
           
        }
    )

def bozkatu(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bozkatu.html',
        {
            
        }
    )

def register(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/register.html',
        {
            
        }
    )

def zaleak(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/zaleak.html',
        {

        }
    )

def menua(request):
    message = Filma.objects.get(pk=1)
    return render(request, 'app/menua.html',
         {
             'message': message
         }
    )

def login(request):
    form = forms.LoginForm()