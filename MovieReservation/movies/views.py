from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MovieSerializer
from rest_framework import status
# Create your views here.

class add_movie(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)

class update_movie(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    pass

class delete_movie(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    pass