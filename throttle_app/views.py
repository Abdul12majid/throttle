from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def welcome_view(request):
    return Response({"message": "Welcome to the throttled API!"})




