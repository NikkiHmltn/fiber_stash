from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Fiber
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def fiber_index(request):
    fiber = Fiber.objects.all()
    return render(request, 'fiber/index.html', {'fiber': fiber})

def fiber_show(request, fiber_id):
    fiber = Fiber.objects.get(id=fiber_id)
    return render(request, 'fiber/show.html', {'fiber': fiber})

class FiberCreate(CreateView):
  model = Fiber
  fields = '__all__'
  success_url = '/fiber'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    # self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/fiber')

class FiberUpdate(UpdateView):
  model = Fiber
  fields = ['types', 'micron', 'description', 'texture']
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/fiber/' + str(self.object.pk))
    
class FiberDelete(DeleteView):
  model = Fiber
  success_url = '/fiber'
