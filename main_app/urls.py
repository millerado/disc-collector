from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('discs/', views.discs_index, name='index'),
  path('discs/<int:disc_id>/', views.discs_details, name='details'),
]