# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    runtime = models.IntegerField()
    release_date = models.DateField()

    @property
    def runtime_formatted(self):
        hours = self.runtime // 60
        minutes = self.runtime % 60
        return f"{hours}:{minutes:02d}"

    @property
    def avg_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / reviews.count()

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
