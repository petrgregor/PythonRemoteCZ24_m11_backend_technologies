"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import movies, home, movie, creator, genre, MoviesView, MoviesTemplateView, MoviesListView, \
    CreatorsListView, CreatorFormView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    #path('movies/', movies, name='movies'),
    #path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/', MoviesTemplateView.as_view(), name='movies'),
    #path('movies/', MoviesListView.as_view(), name='movies'),
    path('movie/<pk>/', movie, name='movie'),

    path('creators/', CreatorsListView.as_view(), name='creators'),
    path('creator/create/', CreatorFormView.as_view(), name='creator_create'),
    path('creator/<pk>/', creator, name='creator'),

    path('genre/<pk>/', genre, name='genre'),
]
