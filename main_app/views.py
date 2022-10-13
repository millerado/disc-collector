from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .models import Disc
from .forms import ThrowForm

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
  throw_form = ThrowForm()
  return render(request, 'discs/details.html', {
    'disc': disc,
    'throw_form': throw_form  
  })

def add_throw(request, disc_id):
  form = ThrowForm(request.POST)
  if form.is_valid():
    new_throw = form.save(commit=False)
    new_throw.disc_id = disc_id
    new_throw.save()
  return redirect('discs_details', disc_id=disc_id)

def signup(request):
  error_message = None
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - Please try again'
  form = UserCreationForm()
  context = {'form': form, 'error': error_message }
  return render(request, 'registration/signup.html', context)

class DiscsCreate(CreateView):
  model = Disc
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DiscsUpdate(UpdateView):
  model = Disc
  fields = ('manufacturer', 'mold', 'plastic', 'flight')

class DiscsDelete(DeleteView):
  model = Disc
  success_url = '/discs/'