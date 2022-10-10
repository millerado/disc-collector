from django.shortcuts import render
from .models import Disc

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