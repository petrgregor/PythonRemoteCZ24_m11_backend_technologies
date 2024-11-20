from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, FormView, UpdateView, DeleteView

from viewer.forms import CreatorForm
from viewer.models import Movie, Creator, Genre


def home(request):
    return render(request, "home.html")


def movies(request):
    # movies_list = Movie.objects.all()
    # context = {'movies': movies_list}
    # return render(request, "movies.html", context)
    return render(request,
                  "movies.html",
                  {'movies': Movie.objects.all(),
                   'genres': Genre.objects.all()})


# Class-based views
## View class
class MoviesView(View):
    def get(self, request):
        return render(request,
                      "movies.html",
                      {'movies': Movie.objects.all(),
                       'genres': Genre.objects.all()})


## TemplateView class
class MoviesTemplateView(TemplateView):
    template_name = "movies.html"
    extra_context = {'movies': Movie.objects.all(), 'genres': Genre.objects.all()}


## ListView
class MoviesListView(ListView):
    # tato view neposílá do template informace o žánrech
    # lze to řešit metodou get_context_data -> tam můžu přidávat cokoliv
    template_name = "movies.html"
    model = Movie
    # pozor: do template se posílají data pod názvem 'object_list'
    # nebo můžu přejmenovat
    context_object_name = 'movies'


def movie(request, pk):
    movies_ = Movie.objects.filter(id=pk)
    if movies_:
        #movie_ = movies_[0]
        #context = {'movie': movie_}
        #return render(request, "movie.html", context)
        return render(request, "movie.html", {'movie': movies_[0]})
    return movies(request)


class CreatorsListView(ListView):
    template_name = "creators.html"
    model = Creator


def creator(request, pk):
    try:
        #creator_ = Creator.objects.get(id=pk)
        #context = {'creator': creator_}
        #return render(request, "creator.html", context)
        return render(request, "creator.html", {'creator': Creator.objects.get(id=pk)})
    except:
        return home(request)


class CreatorFormView(FormView):
    template_name = "form.html"
    form_class = CreatorForm
    success_url = reverse_lazy('creators')

    def form_valid(self, form):
        print("Form is valid")
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Creator.objects.create(
            first_name=cleaned_data["first_name"],
            last_name=cleaned_data["last_name"],
            date_of_birth=cleaned_data["date_of_birth"],
            date_of_death=cleaned_data["date_of_death"],
            nationality=cleaned_data["nationality"],
            biography=cleaned_data["biography"]
        )
        return result

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorCreateView(CreateView):
    template_name = 'form.html'
    form_class = CreatorForm
    success_url = reverse_lazy('creators')

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = CreatorForm
    success_url = reverse_lazy('creators')
    model = Creator

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    model = Creator
    success_url = reverse_lazy('creators')


def genre(request, pk):
    try:
        return render(request, "genre.html", {'genre': Genre.objects.get(id=pk)})
    except:
        return home(request)
