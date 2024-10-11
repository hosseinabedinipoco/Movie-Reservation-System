from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
class UserSerilizer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=False)
    class Meta:
        model = 'User'
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            is_admin = False
        )
        return user