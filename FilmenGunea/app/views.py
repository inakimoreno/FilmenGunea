"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from .models import Filma
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import forms
from . import models

def home(request):
    return render(
        request,
        'app/menua.html',
        {
           
        }
    )

def bozkatu(request):
    return render(
        request,
        'app/bozkatu.html',
        {
            
        }
    )

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        usr = request.POST['usr']
        pswd = request.POST['pswd']
        pswd2 = request.POST['pswd2']
        if pswd==pswd2:
            user = authenticate(username=usr, password=pswd)
            if user is None:
                models.User.objects.create_user(username=usr, password=pswd)
                form = forms.LoginForm()
                return HttpResponseRedirect('../login')

    else:
        return render(
            request,
            'app/register.html',
            {
                'form':form,
            }
        )

def zaleak(request):
    return render(
        request,
        'app/zaleak.html',
        {

        }
    )

def menua(request):
    films_list = Filma.objects.all()
    paginator = Paginator(films_list,4)
    page = request.GET['page']
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        films = paginator.page(1)
    except EmptyPage:
        films = paginator.page(paginator.num_pages)
    return render(request, 'app/menua.html',
         {
             'films': films
         }
    )

def login(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        usr = request.POST['usr']
        pswd = request.POST['pswd']
        user = authenticate(username=usr, password=pswd)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request,'app/menua.html',{})
    else:
        return render(request,'app/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return render(request,'app/menua.html',{})