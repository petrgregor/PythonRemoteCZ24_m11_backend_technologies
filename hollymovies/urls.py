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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import SubmittableLoginView, SignUpView, user_logout
from api.views import Movies, MovieDetail, Creators, CreatorDetail
from hollymovies import settings
from viewer.views import movies, home, movie, creator, genre, MoviesView, MoviesTemplateView, MoviesListView, \
    CreatorsListView, CreatorFormView, CreatorCreateView, CreatorUpdateView, CreatorDeleteView, GenreCreateView, \
    GenreUpdateView, GenreDeleteView, CountryCreateView, CountryUpdateView, CountryDeleteView, MovieCreateView, \
    MovieUpdateView, MovieDeleteView, MovieTemplateView, ImageDetailView, ImageCreateView, ImageUpdateView, \
    ImageDeleteView, search

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    #path('movies/', movies, name='movies'),
    #path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/', MoviesTemplateView.as_view(), name='movies'),
    #path('movies/', MoviesListView.as_view(), name='movies'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<pk>/', MovieTemplateView.as_view(), name='movie'),

    path('creators/', CreatorsListView.as_view(), name='creators'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    path('creator/<pk>/', creator, name='creator'),

    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<pk>/', GenreDeleteView.as_view(), name='genre_delete'),
    path('genre/<pk>/', genre, name='genre'),

    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<pk>/', CountryDeleteView.as_view(), name='country_delete'),

    path('image/create/', ImageCreateView.as_view(), name='image_create'),
    path('image/update/<pk>/', ImageUpdateView.as_view(), name='image_update'),
    path('image/delete/<pk>/', ImageDeleteView.as_view(), name='image_delete'),
    path('image/<pk>/', ImageDetailView.as_view(), name='image'),

    path('search/', search, name='search'),

    #path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # defaultní cesty a views z Djanga

    path('api/movies/', Movies.as_view(), name='api_movies'),
    path('api/movie/<pk>/', MovieDetail.as_view(), name='api_movie'),
    path('api/creators/', Creators.as_view(), name='api_creators'),
    path('api/creator/<pk>/', CreatorDetail.as_view(), name='api_creator'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
