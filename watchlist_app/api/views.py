from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class Reviews(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


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


class StreamPlatformAV(APIView):

    def get(self, request):
        streamPlatforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamPlatforms, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            streamPlatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(streamPlatform)
        return Response(serializer.data)


    def put(self, request, pk):
        try:
            streamPlatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = StreamPlatformSerializer(streamPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            streamPlatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        streamPlatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
