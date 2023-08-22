from django.urls import path
from . import views

urlpatterns = [
    # URL for creating a new checkout
    path('checkout', views.post_checkout, name='post_checkout'),

    # URL for updating an existing checkout
    path('checkout/<int:de_checkout_id>', views.put_checkout, name='put_checkout'),

    # URL for updating the status of a checkout
    path('checkout/status', views.update_checkout_status, name='update_checkout_status'),

    # URL for submitting a checkout
    path('checkout/submit', views.submit_checkout, name='submit_checkout'),

    # URL for getting DECheckout details
    path('checkout/<int:outlet_id>/<int:de_id>/', views.get_de_checkout_details, name='get_de_checkout_details'),

    # URL for creating a new checkout type
    path('checkout/type/', views.post_checkout_type, name='post_checkout_type'),

    # URL for updating an existing checkout type
    path('checkout/type/<int:checkout_type_id>/', views.put_checkout_type, name='put_checkout_type'),

    path('delivery_executives/', views.delivery_executives_view, name='delivery_executives'),
    path('delivery_types/', views.delivery_types_view, name='delivery_types'),

]
