from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.

class signup(APIView):
    def post(self, request):
        pass

class login(APIView):
    pass
