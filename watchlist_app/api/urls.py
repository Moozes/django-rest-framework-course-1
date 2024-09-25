from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('watch/' , WatchListAV.as_view()),
    path('watch/<int:pk>' , WatchDetailAV.as_view()),
    path('stream-platform/' , StreamPlatformAV.as_view()),
    path('stream-platform/<int:pk>' , StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]
