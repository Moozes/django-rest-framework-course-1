from django.urls import path
from watchlist_app.api.views import movie_detail, movie_list
urlpatterns = [
    path('list/' , movie_list),
    path('<int:pk>' , movie_detail),
]
