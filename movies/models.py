# movies/models.py
from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=20)
    rating = models.CharField(max_length=10, choices=[("G", "General"), ("PG", "Parental Guidance"), ("R", "Restricted")])
    synopsis = models.TextField(null=True, blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="added_movies"
    )

    def __str__(self):
        return self.title


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="orders")
    ordered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movie_orders"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.movie.title} by {self.ordered_by}"
