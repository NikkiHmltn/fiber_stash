from django.shortcuts import render
from django.http import HttpResponse
from .models import Fiber


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def fiber_index(request):
    fiber = Fiber.objects.all()
    return render(request, 'fiber/index.html', {'fiber': fiber})
