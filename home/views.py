from django.shortcuts import render

# Create your views here.
from django import HttpResponse
def home(request):
    return HttpResponse("hey i am a django lover....")