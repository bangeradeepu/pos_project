from django.urls import path, include
from . import views

urlpatterns = [
    path('brands/', include('company.brands.urls')), 
    path('locations/', include('company.locations.urls')), 
    path('outlets/', include('company.outlets.urls')), 
    
    # URLs for Brand model
    path('brand/', views.BrandCreateView.as_view(), name='brand-create'),
    path('brand/<int:brand_id>/', views.BrandRetrieveView.as_view(), name='brand-retrieve'),
    path('brand/<int:brand_id>/update/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('brand/<int:brand_id>/delete/', views.BrandDeleteView.as_view(), name='brand-delete'),

    # URLs for UserCompanyConnection model
    path('connection/', views.UserCompanyConnectionCreateView.as_view(), name='connection-create'),
    path('connection/<int:connection_id>/', views.UserCompanyConnectionRetrieveView.as_view(), name='connection-retrieve'),
    path('connection/<int:connection_id>/update/', views.UserCompanyConnectionUpdateView.as_view(), name='connection-update'),
    path('connection/<int:connection_id>/delete/', views.UserCompanyConnectionDeleteView.as_view(), name='connection-delete'),

    path('get_location_details/', views.get_location_details_view, name='get_location_details'),
    path('get_distance_from_outlet/', views.get_distance_from_outlet_view, name='get_distance_from_outlet'),
    path('init_delivery_type/', views.init_delivery_type_view, name='init_delivery_type'),
    path('create_nearest_outlet_promise/', views.create_nearest_outlet_promise_view, name='create_nearest_outlet_promise'),


]
