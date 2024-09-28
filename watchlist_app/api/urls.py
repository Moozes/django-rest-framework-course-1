from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    Reviews,
    ReviewDetail,
    ReviewCreate
)

router = DefaultRouter()
router.register('stream', StreamPlatformAV, basename='stream')

urlpatterns = [
    path('watch/' , WatchListAV.as_view()),
    path('watch/<int:pk>' , WatchDetailAV.as_view()),

    path('watch/<int:pk>/reviews/create' , ReviewCreate.as_view()),
    path('watch/<int:pk>/reviews/' , Reviews.as_view()),
    path('watch/reviews/<int:pk>' , ReviewDetail.as_view()),

    path('', include(router.urls))
]
