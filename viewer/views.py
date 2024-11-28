from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Avg, Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, FormView, UpdateView, DeleteView, DetailView

from accounts.models import Profile
from viewer.forms import CreatorForm, GenreModelForm, CountryModelForm, MovieModelForm, ReviewModelForm, ImageModelForm
from viewer.models import Movie, Creator, Genre, Country, Review, Image


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


class MovieTemplateView(TemplateView):
    template_name = "movie.html"

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        if not Movie.objects.filter(id=pk).exists():
            return HttpResponseRedirect(reverse_lazy('movies'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        movie_ = Movie.objects.filter(id=pk)
        if movie_:
            context['movie'] = movie_[0]
            context['form_review'] = ReviewModelForm
            rating_avg = movie_[0].reviews.aggregate(Avg('rating'))['rating__avg']
            #print(f"movie_[0].reviews.aggregate(Avg('rating')) = '{movie_[0].reviews.aggregate(Avg('rating'))}'")
            #print(f"movie_[0].reviews.aggregate(Max('rating')) = '{movie_[0].reviews.aggregate(Max('rating'))}'")
            #print(f"rating_avg: {rating_avg}")
            context['rating_avg'] = rating_avg
            return context
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        reviews = Review.objects.filter(movie=context['movie'],
                                        reviewer=Profile.objects.get(user=request.user))
        if reviews.exists():
            review_ = reviews[0]
            review_.rating = request.POST.get('rating')
            review_.comment = request.POST.get('comment')
            review_.save()
        else:
            Review.objects.create(
                movie=context['movie'],
                reviewer=Profile.objects.get(user=request.user),
                rating=request.POST.get('rating'),
                comment=request.POST.get('comment')
            )
        movie_ = context['movie']
        rating_avg = movie_.reviews.aggregate(Avg('rating'))['rating__avg']
        #print(f"rating_avg: {rating_avg}")
        context['rating_avg'] = rating_avg
        return render(request, 'movie.html', context)


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')
    model = Movie
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


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


class CreatorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CreatorForm
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.add_creator'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CreatorForm
    success_url = reverse_lazy('creators')
    model = Creator
    permission_required = 'viewer.change_creator'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CreatorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Creator
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.delete_creator'


def genre(request, pk):
    try:
        return render(request, "genre.html", {'genre': Genre.objects.get(id=pk)})
    except:
        return home(request)


class GenreCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_genre'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    success_url = reverse_lazy('home')
    model = Genre
    permission_required = 'viewer.change_genre'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Genre
    success_url = reverse_lazy('home')
    permission_required = 'viewer.delete_genre'


class CountryCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_country'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CountryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    success_url = reverse_lazy('home')
    model = Country
    permission_required = 'viewer.change_country'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class CountryDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Country
    success_url = reverse_lazy('home')
    permission_required = 'viewer.delete_country'


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'


class ImageCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.add_image'

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('home')
    permission_required = 'viewer.change_image'
    model = Image

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')
    permission_required = 'viewer.delete_image'
    model = Image
