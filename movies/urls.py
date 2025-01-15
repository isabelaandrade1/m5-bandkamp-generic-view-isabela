# movies/urls.py
from django.urls import path
from .views import MovieView, MovieDetailView, MovieOrderDetailView

urlpatterns = [
    path('movies/', MovieView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/orders/', MovieOrderDetailView.as_view(), name='movie-order'),
]

