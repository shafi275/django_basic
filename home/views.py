from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   peoples=[
    {'name':'shariyar shafi','age':24},
    {'name': 'rashedul islam','age':26},
    {'name': 'pk taskin','age':28}
   ]
   return render(request,"index.html",context={'peoples':peoples})
def success_page(request):
    return HttpResponse(" <h1>Hey this is a success page </h1>")