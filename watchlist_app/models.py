from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=200)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.watchlist.title} (rating: {self.rating})"