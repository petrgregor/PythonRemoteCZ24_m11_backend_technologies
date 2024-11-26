from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import *


class MovieAdmin(ModelAdmin):

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        for obj in queryset:
            obj.description = ""
            obj.save()

    ordering = ['title_orig', 'year']  # ['year', 'id']
    list_display = ['id', 'title_orig', 'title_cz', 'year']
    list_display_links = ['id', 'title_orig']
    list_per_page = 20
    list_filter = ['genres', 'countries']
    search_fields = ['title_orig', 'title_cz']
    actions = ['cleanup_description']

    fieldsets = [
        ('Titles',
         {'fields':
             [
                 'title_orig',
                 'title_cz'
             ]
         }
         ),
        ('External information',
         {'fields':
              [
                  'genres',
                  'countries',
                  'year',
                  'length'
               ],
          'description': 'These fields are going to be filled with data parsed from external databases.'
          }
         ),
        ('Creators',
         {'fields':
              ['directors',
               'actors'
               ],
          'description': 'Information about creators.'
          }),
        ('User information',
         {'fields':
              ['description']
          }
         ),
        ('Internal information',
         {'fields':
             [
                 'created',
                 'updated'
             ]
         }
         )
    ]
    readonly_fields = ['created', 'updated']


admin.site.register(Country)
admin.site.register(Creator)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
