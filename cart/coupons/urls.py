from django.urls import path
from . import views

urlpatterns = [
    # Coupon URLs
    path('coupons/', views.create_coupon, name='create_coupon'),
    path('coupons/<int:pk>/', views.update_coupon, name='update_coupon'),
    path('coupons/<int:pk>/', views.delete_coupon, name='delete_coupon'),
    path('coupons/', views.get_coupons, name='get_coupons'),

    # Customer Coupon URLs
    path('customer_coupon/', views.create_customer_coupon, name='create_customer_coupon'),
    path('customer_coupon/', views.update_customer_coupon, name='update_customer_coupon'),
    path('customer_coupon/', views.delete_customer_coupon, name='delete_customer_coupon'),
    path('customer_coupon/', views.get_customer_coupons, name='get_customer_coupons'),

    # Influencer Coupon URLs
    path('influencer_coupon/', views.create_influencer_coupon, name='create_influencer_coupon'),
    path('influencer_coupon/', views.update_influencer_coupon, name='update_influencer_coupon'),
    path('influencer_coupon/', views.delete_influencer_coupon, name='delete_influencer_coupon'),
    path('influencer_coupon/', views.get_influencer_coupons, name='get_influencer_coupons'),

    path('create_coupon_outlet_link/', views.create_coupon_outlet_link, name='create_coupon_outlet_link'),
]
