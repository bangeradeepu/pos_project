from django.urls import path
from . import views

urlpatterns = [
    # URLs for GeneralSettings model
    path('timings/', views.timings_post_view, name='timings-post'),
    path('status/', views.status_post_view, name='status-post'),
    path('create-additional-charge/', views.create_additional_charge, name='create_additional_charge'),
    path('update-additional-charge/<int:charge_id>/', views.update_additional_charge, name='update_additional_charge'),
    path('get-general-settings/', views.get_general_settings, name='get_general_settings'),
    path('update-outlets/', views.update_outlets, name='update_outlets'),
]
