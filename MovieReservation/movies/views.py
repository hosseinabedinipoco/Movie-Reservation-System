from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class add_movie(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        pass

class update_movie(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    pass

class delete_movie(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    pass