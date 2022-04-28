"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from .models import Filma, Bozkatzailea, User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    return render(
        request,
        'app/menua.html',
        {
           
        }
    )

@login_required
def bozkatu(request):
    mezua_egoera = ''
    mezua_filma = ''
    if request.method == 'POST':
        try:
            voter = Bozkatzailea.objects.get(erabiltzailea_id=request.user)
        except:
            voter = Bozkatzailea(erabiltzailea_id=request.user)
            voter.save()
        if Filma.objects.get(pk=request.POST['selectFilm']) in voter.gogokofilmak.all():
            mezua_egoera = f"{Filma.objects.get(pk=request.POST['selectFilm']).izenburua} dagoeneko bozkatu duzu!"
        else:
            voter.gogokofilmak.add(request.POST['selectFilm'])
            voter.save()
            mezua_egoera = "Bozkaketa ondo joan da"
            mezua_filma = f"Zure bozketa: {Filma.objects.get(pk=request.POST['selectFilm']).izenburua}"
    films = Filma.objects.all()
    return render(
        request,
        'app/bozkatu.html',
        {
            'films':films,
            "mezua_egoera":mezua_egoera,
            "mezua_filma":mezua_filma
        }
    )

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        usr = request.POST['usr']
        pswd = request.POST['pswd']
        pswd2 = request.POST['pswd2']
        if pswd==pswd2:
            user = User.objects.filter(username=usr)
            if user.count() == 0:
                models.User.objects.create_user(username=usr, password=pswd)
                form = forms.LoginForm()
                return HttpResponseRedirect('../login')
            else:
                mezua = "Erabiltzailea dagoekeo existitzen da"
        else:
            mezua = "Pasahitzek ez dute koinziditzen"
        return render(
            request,
            'app/register.html',
            {
                'form': form,
                'mezua': mezua
            }
        )
    else:
        return render(
            request,
            'app/register.html',
            {
                'form':form,
            }
        )
@login_required
def zaleak(request):
    films = Filma.objects.all()
    if request.method == "POST":
        voters = Bozkatzailea.objects.filter(gogokofilmak=request.POST['selectFilm'])
        selectedFilm = Filma.objects.get(pk=request.POST['selectFilm'])
        return render(request, 'app/zaleak.html',{'films':films,'bozkatzaileak':voters,'selectedFilm':selectedFilm})
    return render(
        request,
        'app/zaleak.html',
        {
            'films':films
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
    next='/login/'
    if request.method == 'POST':
        next = request.POST['next']
        usr = request.POST['usr']
        pswd = request.POST['pswd']
        user = authenticate(username=usr, password=pswd)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect(next)
        mezua = "Erabiltzaile edo pasahitza okerra"
        return render(request,'app/login.html',{'form':form, "mezua":mezua})
    else:
        if 'next' in request.GET:
            next=request.GET['next']
        return render(request,'app/login.html',{'form':form, 'next':next})

@login_required
def logout(request):
    auth_logout(request)
    return render(request,'app/menua.html',{})