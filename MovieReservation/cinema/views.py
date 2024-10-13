from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import Is_admin
from rest_framework.response import Response
from .serializers import CinemaSerializer
from rest_framework import status
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
    

class delete_Cinema(APIView):
    permission_classes = [Is_admin, IsAuthenticated]        
