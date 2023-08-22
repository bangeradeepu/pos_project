from django.urls import path
from .views import CustomersView, AddressView

urlpatterns = [
    # Customers URLs
    path('customers/', CustomersView.as_view(), name='customers-list'),
    path('customers/<int:pk>/', CustomersView.as_view(), name='customers-detail'),
    # CustomerAddresses URLs
    path('customer_addresses/', AddressView.as_view(), name='customer-addresses-list'),
    path('customer_addresses/<int:pk>/', AddressView.as_view(), name='customer-addresses-detail'),
]
