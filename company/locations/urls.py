from django.urls import path
from . import views

urlpatterns = [
    path('location/json/validation/', views.location_json_validation, name='location-json-validation'),
    path('layers/validation/', views.layers_validation, name='layers-validation'),
    path('distances/validation/', views.distances_validation, name='distances-validation'),
    path('charges/validation/', views.charges_validation, name='charges-validation'),
    path('charges/delete/validation/', views.charges_delete_validation, name='charges-delete-validation'),
    path('is-serviceable/validation/', views.is_serviceable_validation, name='is-serviceable-validation'),
]
