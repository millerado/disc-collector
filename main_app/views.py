from ast import Del
from django.shortcuts import render
from .models import Disc
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def discs_index(request):
  discs = Disc.objects.all()
  return render(request, 'discs/index.html', {'discs':discs })

def discs_details(request, disc_id):
  disc = Disc.objects.get(id=disc_id)
  return render(request, 'discs/details.html', {'disc': disc})

class DiscsCreate(CreateView):
  model = Disc
  fields = '__all__'

class DiscsUpdate(UpdateView):
  model = Disc
  fields = ('manufacturer', 'mold', 'plastic', 'flight')

class DiscsDelete(DeleteView):
  model = Disc
  success_url = '/discs/'