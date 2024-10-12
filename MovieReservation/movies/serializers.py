from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_genre(self, data):
        if data not in ['comedy', 'drama', 'social']:
            raise serializers.ValidationError("invalid genre")
        return data

    def create(self, validated_data):
        movie = Movie.objects.create(
            title = validated_data['title'],
            description = validated_data['description'],
            time_in_minute = validated_data['time'],
            director = validated_data['director'],
            genre = validated_data['genre']
        )    
        return movie