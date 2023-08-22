from django.urls import path
from . import views

urlpatterns = [
    path('update_outlet/', views.variant_outlet_link_view, name='update_outlet'),
    path('update_category/', views.update_category, name='update_category'),
    path('create_category/', views.create_category, name='create_category'),
    path('delete_category/', views.delete_category, name='delete_category'),
    path('get_variants/', views.get_variants, name='get_variants'),
    path('create_variant/', views.create_variant, name='create_variant'),
    path('update_variant/', views.update_variant, name='update_variant'),
    path('delete_variant/', views.delete_variant, name='delete_variant'),
]
