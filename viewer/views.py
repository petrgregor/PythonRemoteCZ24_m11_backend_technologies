from django.shortcuts import render

from viewer.models import Movie


def home(request):
    return render(request, "home.html")


def movies(request):
    # movies_list = Movie.objects.all()
    # context = {'movies': movies_list}
    # return render(request, "movies.html", context)
    return render(request, "movies.html", {'movies': Movie.objects.all()})


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie_ = Movie.objects.get(id=pk)
        context = {'movie': movie_}
        return render(request, "movie.html", context)
    return movies(request)
