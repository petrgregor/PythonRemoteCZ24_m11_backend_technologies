from django.shortcuts import render

from viewer.models import Movie, Creator


def home(request):
    return render(request, "home.html")


def movies(request):
    # movies_list = Movie.objects.all()
    # context = {'movies': movies_list}
    # return render(request, "movies.html", context)
    return render(request, "movies.html", {'movies': Movie.objects.all()})


def movie(request, pk):
    movies_ = Movie.objects.filter(id=pk)
    if movies_:
        #movie_ = movies_[0]
        #context = {'movie': movie_}
        #return render(request, "movie.html", context)
        return render(request, "movie.html", {'movie': movies_[0]})
    return movies(request)


def creator(request, pk):
    try:
        #creator_ = Creator.objects.get(id=pk)
        #context = {'creator': creator_}
        #return render(request, "creator.html", context)
        return render(request, "creator.html", {'creator': Creator.objects.get(id=pk)})
    except:
        return home(request)
