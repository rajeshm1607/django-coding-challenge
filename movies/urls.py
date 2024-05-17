# movies/urls.py
from django.urls import path
from .views import MovieListCreateView, MovieDetailView, ReviewListCreateView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]
