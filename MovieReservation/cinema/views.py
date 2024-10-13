from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import Is_admin
from rest_framework.response import Response
from .serializers import CinemaSerializer
from rest_framework import status
from .models import Cinema
from django.shortcuts import get_object_or_404
# Create your views here.

class Add_cinema(APIView):
    permission_classes = [Is_admin, IsAuthenticated]
    def post(self, request):
        cinema = CinemaSerializer(data=request.data)
        if cinema.is_valid():
            cinema.save()
            return Response(cinema.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cinema.errors, status=status.HTTP_400_BAD_REQUEST)

class Update_Cinema(APIView):
    permission_classes = [IsAuthenticated, Is_admin]
    def put(self, request, id):
        cinema = get_object_or_404(Cinema, pk=id)
        serializer = CinemaSerializer(cinema, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class delete_Cinema(APIView):
    permission_classes = [Is_admin, IsAuthenticated]        
    def delete(self, request, id):
        cinema = get_object_or_404(Cinema, pk=id)
        cinema.delete()
        return Response({'message':"deleted"}, status=status.HTTP_204_NO_CONTENT)