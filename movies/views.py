from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    user_rating = 0
    if request.user.is_authenticated:
        rating = Rating.objects.filter(
            user=request.user,
            movie=movie
        ).first()
        if rating:
            user_rating = rating.score

    return render(request, "movies/movie_detail.html", {
        "movie": movie,
        "user_rating": user_rating,
    })

def rate_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        score = float(request.POST["score"])

        Rating.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={"score": score}
        )

    return redirect("movie_detail", pk=movie.id)


    return render(request, "movies/rate_movie.html", {"movie": movie})