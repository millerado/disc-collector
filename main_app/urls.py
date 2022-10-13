from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('discs/', views.discs_index, name='index'),
  path('discs/<int:disc_id>/', views.discs_details, name='discs_details'),
  path('discs/create', views.DiscsCreate.as_view(), name='discs_create'),
  path('disc/<int:pk>/update', views.DiscsUpdate.as_view(), name='discs_update'),
  path('disc/<int:pk>/delete', views.DiscsDelete.as_view(), name='discs_delete'),
  path('disc/<int:pk>/add_throw', views.add_throw, name='add_throw'),
  path('accounts/signup', views.signup, name='signup'),
]