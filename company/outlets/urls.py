from django.urls import path
from . import views

urlpatterns = [
    # URLs for Outlets model
    path('outlets/', views.get_outlets, name='get_outlets'),
    path('outlets/create/', views.create_outlet, name='create_outlet'),
    path('outlets/update/', views.update_outlet, name='update_outlet'),
    
    # URLs for CompanyOutlets model
    path('company_outlets/', views.get_company_outlets, name='get_company_outlets'),
    path('company_outlets/create/', views.create_company_outlet, name='create_company_outlet'),
    path('company_outlets/update/', views.update_company_outlet, name='update_company_outlet'),
]
