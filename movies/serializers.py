# movies/serializers.py
from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'rating', 'movie']
        extra_kwargs = {
            'movie': {'required': True}
        }

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    runtime_formatted = serializers.ReadOnlyField()
    avg_rating = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'runtime', 'runtime_formatted', 'release_date', 'avg_rating', 'reviews']
