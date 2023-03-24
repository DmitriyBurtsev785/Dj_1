from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def sample_controller(request):
    return HttpResponse("Hello world!")