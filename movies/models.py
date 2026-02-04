from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, default="Unknown")
    director = models.CharField(max_length=100, default="Unknown")
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/")


    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.score}"
