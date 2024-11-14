from django.shortcuts import render

from viewer.models import Movie


def home(request):
    return render(request, "home.html")


def movies(request):
    # movies_list = Movie.objects.all()
    # context = {'movies': movies_list}
    # return render(request, "movies.html", context)
    return render(request, "movies.html", {'movies': Movie.objects.all()})
