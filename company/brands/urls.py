from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.get_brands, name='get_brands'),
    path('brands/create/', views.create_brand, name='create_brand'),
    path('brands/update/', views.update_brand, name='update_brand'),
    path('brands/delete/', views.delete_brand, name='delete_brand'),
    path('outlets/add_brand/', views.add_brand_to_outlet, name='add_brand_to_outlet'),
    path('outlets/remove_brand/', views.remove_brand_from_outlet, name='remove_brand_from_outlet'),
]
