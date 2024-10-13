from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import Is_admin
# Create your views here.

class Add_cinema(APIView):
    permission_classes = [Is_admin, IsAuthenticated]

class Update_Cinema(APIView):
    permission_classes = [IsAuthenticated, Is_admin]

class delete_Cinema(APIView):
    permission_classes = [Is_admin, IsAuthenticated]        
