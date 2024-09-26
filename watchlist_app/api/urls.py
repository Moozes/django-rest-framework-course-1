from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, Reviews, ReviewDetail

urlpatterns = [
    path('watch/' , WatchListAV.as_view()),
    path('watch/<int:pk>' , WatchDetailAV.as_view()),
    path('stream-platform/' , StreamPlatformAV.as_view()),
    path('stream-platform/<int:pk>' , StreamPlatformDetailAV.as_view()),
    path('stream-platform/<int:pk>/reviews/' , Reviews.as_view()),
    path('stream-platform/reviews/<int:pk>' , ReviewDetail.as_view()),
]
