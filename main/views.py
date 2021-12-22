import os

from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
# Create your views here.

# from .films_content import Films


def index(request):
    return render(request, 'main/index.html')

def movies(request):
    movies = Films.objects.all()
    categories = Category.objects.all()
    data = {"movies": movies, "category": categories}
    return render(request, 'main/movies.html', context=data)

def form(request):
    return render(request, 'main/form.html')

def about_us(request):

    return render(request, 'main/about_us.html')

def signupuser(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        return render(request, 'main/signupuser.html' , {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'main/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'main/signupuser.html', {'form': UserCreationForm(), 'error': 'Password is not valid!'})

@login_required
def showAdminPanel(request):
    if request.user.is_superuser:
        return render(request, 'main/tmp.html')
    else:
        return redirect('index')

@login_required
def showFilms(request):
    if request.user.is_superuser:
        allFilms= Films.objects.all()
        return render(request, 'main/adminFilms.html', {'films': allFilms})
    else:
        return redirect('index')

def getCategoryID(id):
    return Category.objects.filter(id=id).first()

def getFilmByID(id):
    return Films.objects.filter(id=id).first()

def updateFilm(request):
    film = Films.objects.filter(id=request.POST['film_id']).first()
    film.title = request.POST['title']
    film.genre = request.POST['genre']
    film.desc = request.POST['desc']
    film.categoryID = getCategoryID(request.POST['cat_id'])
    film.image = request.FILES.get('film_image', default='img/default.png')
    film.save()
    return True

def deleteFilm(request):
    Films.objects.filter(id=request.GET['film_id']).delete()
    return True

def createFilm(request):
    # film = Films()
    # film.title = request.POST['title']
    # film.genre = request.POST['genre']
    # film.desc = request.POST['desc']
    # film.rating = request.POST['rating']
    # film.categoryID = getCategoryID(request.POST['categoryID'])
    #
    # if len(request.FILES) != 0:
    #     film.image = request.FILES['film_image']
    #
    # film.save()
    Films.objects.create(title=request.POST['title'], genre=request.POST['genre'], desc=request.POST['desc'],
                         rating=request.POST['rating'],
                         categoryID=getCategoryID(request.POST['categoryID']),
                         image=request.FILES.get('film_image', default='img/default.png'))
    return True

@login_required
def createAdminFilm(request):
    if request.method == 'GET':
        return render(request, 'main/createFilm.html')
    if request.method == 'POST':
        if createFilm(request):
            return redirect('showFilms')
        return redirect('admin')

@login_required
def updateAdminFilm(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'main/updateFilm.html', context={'film':getFilmByID(request.GET['film_id'])})
        if request.method == 'POST':
            if updateFilm(request):
               return redirect('showFilms')
    else:
        return redirect('index')

@login_required
def deleteAdminFilm(request):
    if request.user.is_superuser:
        if request.method=='GET':
            if deleteFilm(request):
                return redirect('showFilms')
        else:
            return redirect('admin')
    else:
        return redirect('index')

@login_required
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('loginuser')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('index')

