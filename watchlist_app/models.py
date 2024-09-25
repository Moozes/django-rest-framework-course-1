from django.db import models

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