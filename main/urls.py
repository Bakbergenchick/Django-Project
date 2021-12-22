from django.conf.urls.static import static
from django.urls import path

from Djlab3 import settings
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('movies/', views.movies, name= 'movies'),
    path('form/', views.form, name='form'),
    path('about_us/', views.about_us, name='about_us'),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Admin Panel
    # My Admin
    path('Myadmin/', views.showAdminPanel, name="admin"),
    path('MyFilms/', views.showFilms, name ="showFilms"),
    path('Myadmin/createFilm/', views.createAdminFilm, name="createFilm"),
    path('Myadmin/updateFilm/', views.updateAdminFilm, name="updateFilm"),
    path('Myadmin/deleteFilm/', views.deleteAdminFilm, name="deleteFilm"),

]