from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import UserSerilizer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class signup(APIView):
    def post(self, request):
        user = UserSerilizer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = get_object_or_404(User, username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'Icorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

            
