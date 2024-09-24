from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"




# def value_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Value is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     name = serializers.CharField(validators=[value_length])
#     description = serializers.CharField(validators=[value_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and description should not be the same')
#         return data
    
#    def validate_name(self, value):
#        if len(value) < 2:
#            raise serializers.ValidationError("Name is too short")
#        return value