from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("hey i am a django lover....")
def success_page(request):
    return HttpResponse(" <h1>Hey this is a success page </h1>")