from datetime import date

from django.db.models import Model, CharField, DateField, ForeignKey, SET_NULL, TextField, ManyToManyField, \
    DateTimeField, IntegerField, CASCADE, ImageField, FloatField

from accounts.models import Profile


class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    def __repr__(self):
        return f"Country(name={self.name})"

    def __str__(self):
        return self.name


class Creator(Model):
    first_name = CharField(max_length=32, null=True, blank=True)
    last_name = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    nationality = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators_nationality')
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name', 'date_of_birth']

    def __repr__(self):
        return f"Creator(first_name={self.first_name}, last_name={self.last_name}, date_of_birth={self.date_of_birth})"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.date_of_birth})"
        # "Martin Novák (1975-05-06)"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        """ Tomas Jasko
        if self.date_of_birth:
            end_date = self.date_of_death or date.today()
            years = end_date.year - self.date_of_birth.year
            if (end_date.month < self.date_of_birth.month) or (
                    end_date.month == self.date_of_birth.month and end_date.day < self.date_of_birth.day):
                years -= 1
            return years
        return None """
        if self.date_of_birth:
            end_date = self.date_of_death or date.today()
            return (end_date.year - self.date_of_birth.year -
                    ((end_date.month, end_date.day) < (self.date_of_birth.month, self.date_of_birth.day)))
        return None


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    year = IntegerField(null=True, blank=True)
    length = IntegerField(null=True, blank=True)
    directors = ManyToManyField(Creator, blank=True, related_name='directing')
    actors = ManyToManyField("viewer.Creator", blank=True, related_name='acting')
    countries = ManyToManyField(Country, blank=True, related_name='movies')
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    description = TextField(blank=True)
    rating = FloatField(null=True, blank=True)
    page_views = IntegerField(default=0)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_orig']

    def __repr__(self):
        return f"Movie(title_orig={self.title_orig})"

    def __str__(self):
        return f"{self.title_orig} ({self.year})"

    def length_format(self):
        # 127 min -> 2:07
        if self.length:
            hours = self.length // 60
            minutes = self.length % 60
            if minutes < 10:
                minutes = f"0{minutes}"
            return f"{hours}:{minutes}"
        return "neznámá"


class Review(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE, null=False, blank=False, related_name='reviews')
    reviewer = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=False, related_name='reviews')
    rating = IntegerField(null=True, blank=True)  # 1-10
    comment = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __repr__(self):
        return (f"Review(movie={self.movie}, reviewer={self.reviewer}, "
                f"rating={self.rating}, comment={self.comment})")

    def __str__(self):
        return (f"Reviewer: {self.reviewer}, movie: {self.movie}, rating={self.rating}, "
                f"comment: {self.comment[:50]}")


class Image(Model):
    image = ImageField(upload_to='images/', default=None, null=False, blank=False)
    movie = ForeignKey(Movie, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    actors = ManyToManyField(Creator, blank=True, related_name='images')
    description = TextField(null=True, blank=True)

    def __repr__(self):
        return (f"Image(image={self.image}, "
                f"movie={self.movie}, "
                f"actors={self.actors}, "
                f"description={self.description})")

    def __str__(self):
        return f"Image: {self.image}, {self.description}"
