from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .models import Disc, Bag
from .forms import ThrowForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def discs_index(request):
  discs = Disc.objects.filter(user=request.user)
  return render(request, 'discs/index.html', {'discs':discs })

@login_required
def discs_details(request, disc_id):
  disc = Disc.objects.get(id=disc_id)
  throw_form = ThrowForm()
  bags = Bag.objects.exclude(id__in=disc.bags.all().values_list('id'))
  return render(request, 'discs/details.html', {
    'disc': disc,
    'throw_form': throw_form,
    'bags': bags,  
  })

@login_required
def assoc_bag(request, disc_id, bag_id):
  Disc.objects.get(id=disc_id).bags.add(bag_id)
  return redirect('discs_details', disc_id=disc_id)

@login_required
def remove_bag(request, disc_id, bag_id):
  Disc.objects.get(id=disc_id).bags.remove(bag_id)
  return redirect('discs_details', disc_id=disc_id)

@login_required

@login_required
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

class DiscsCreate(LoginRequiredMixin, CreateView):
  model = Disc
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DiscsUpdate(LoginRequiredMixin, UpdateView):
  model = Disc
  fields = ('manufacturer', 'mold', 'plastic', 'flight')

class DiscsDelete(LoginRequiredMixin, DeleteView):
  model = Disc
  success_url = '/discs/'

@login_required
def bags_index(request):
  bags = Bag.objects.all()
  return render(request, 'bags/index.html', { 'bags': bags })

class BagsCreate(LoginRequiredMixin, CreateView):
  model = Bag
  fields = '__all__'
  success_url = '/bags/'

class BagsUpdate(LoginRequiredMixin, UpdateView):
  model = Bag
  fields = ('name',)
  success_url = '/bags/'

class BagsDelete(LoginRequiredMixin, DeleteView):
  model = Bag
  success_url = '/bags/'
