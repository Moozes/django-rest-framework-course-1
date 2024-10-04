from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.api.permissions import AdminOrReadOnly, OwnerOrReadOnly

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        # watchlist not found error is not handled, this will cause 500 status response
        watchlist = WatchList.objects.get(pk=pk)

        user = self.request.user
        user_reviews = Review.objects.filter(watchlist=watchlist, user=user)
        if user_reviews.exists():
            raise ValidationError("You have already reviewed this wathchlist")
        

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (serializer.validated_data['rating'] + watchlist.avg_rating)/2
        watchlist.number_rating += 1
        watchlist.save()

        serializer.save(watchlist=watchlist, user=user)


class Reviews(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # here we are requiring the user to be authenticated to access review list
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [OwnerOrReadOnly]


class WatchListAV(APIView):

    def get(self, request):
        watchList = WatchList.objects.all()
        serializer = WatchListSerializer(watchList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watch)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformAV(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer