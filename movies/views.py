from django.shortcuts import render, get_object_or_404
from .models import Movie, Rating

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        score = int(request.POST["score"])
        Rating.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={"score": score}
        )

    return render(request, "movies/movie_detail.html", {"movie": movie})
def rate_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        score = request.POST["score"]
        Rating.objects.create(
            user=request.user,
            movie=movie,
            score=score
        )

    return render(request, "movies/rate_movie.html", {"movie": movie})