from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "director")
    search_fields = ("title", "director")
    list_filter = ("genre",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "score")
