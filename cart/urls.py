from django.urls import path, include
from . import views

urlpatterns = [
    path('coupons/', include('cart.coupons.urls')), 
    path('cart/', views.post_validation_view, name='post_cart'),
    path('cart/update/', views.put_validation_view, name='put_cart'),
    path('cart/delete/', views.delete_validation_view, name='delete_cart'),
]
