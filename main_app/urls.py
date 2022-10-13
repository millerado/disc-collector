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
  path('bags/', views.bags_index, name='bags_index'),
  path('bags/create/', views.BagsCreate.as_view(), name='bags_create'),
  path('bags/<int:pk>/update/', views.BagsUpdate.as_view(), name='bags_update'),
  path('bags/<int:pk>/delete/', views.BagsDelete.as_view(), name='bags_delete'),
  path('discs/<int:disc_id>/assoc_bag/<int:bag_id>/', views.assoc_bag, name='assoc_bag'),
  path('discs/<int:disc_id>/remove_bag/<int:bag_id>/', views.remove_bag, name='remove_bag'),
]