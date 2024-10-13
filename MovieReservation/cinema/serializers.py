from rest_framework import serializers
from .models import Cinema

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"

    def validate_city(self, data):
        if data not in ["Tehran", "Rasht", "Babolsar"]:
            raise serializers.ValidationError("invalid city")
        return data
    
    def create(self, validated_data):
        cinema = Cinema.objects.create(
            name = validated_data['name'],
            city = validated_data['city'],
            capacity = validated_data['capacity'],
            address = validated_data['address']
        )
        return cinema