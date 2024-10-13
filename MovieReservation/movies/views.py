from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import MovieSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Movie
from users.permissions import Is_admin
# Create your views here.

class add_movie(APIView):
    permission_classes = [IsAuthenticated, Is_admin]
    def post(self, request):
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)

class update_movie(APIView):
    permission_classes = [IsAuthenticated, Is_admin]
    def put(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        movie_serializer = MovieSerializer(movie, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class delete_movie(APIView):
    permission_classes = [IsAuthenticated, Is_admin]
    def delete(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        movie.delete()
        return Response({"message":"deleted"}, status=status.HTTP_204_NO_CONTENT)
