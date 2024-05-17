# movies/views.py
from rest_framework import generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        runtime_filter = self.request.query_params.get('runtime', None)
        if runtime_filter:
            runtime_filter = runtime_filter.split(':')
            if len(runtime_filter) == 2:
                try:
                    runtime = int(runtime_filter[1])
                    if runtime_filter[0] == 'lt':
                        queryset = queryset.filter(runtime__lt=runtime)
                    elif runtime_filter[0] == 'gt':
                        queryset = queryset.filter(runtime__gt=runtime)
                except ValueError:
                    pass
        return queryset

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        movie_id = self.request.query_params.get('movie_id', None)
        min_rating = self.request.query_params.get('min_rating', None)
        max_rating = self.request.query_params.get('max_rating', None)
        rating_gt = self.request.query_params.get('rating_gt', None)
        rating_lt = self.request.query_params.get('rating_lt', None)
        
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)
        if max_rating:
            queryset = queryset.filter(rating__lte=max_rating)
        if rating_gt:
            queryset = queryset.filter(rating__gt=rating_gt)
        if rating_lt:
            queryset = queryset.filter(rating__lt=rating_lt)
        return queryset
