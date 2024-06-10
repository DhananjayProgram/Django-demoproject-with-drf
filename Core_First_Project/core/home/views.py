from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hi, /n I am a Django Server")