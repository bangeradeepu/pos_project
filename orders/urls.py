from django.urls import path, include
from . import views

urlpatterns = [
    path('generalSettings/', include('orders.generalSettings.urls')), 

    path('orders/<int:order_id>/', views.get_order, name='get_order'),
    path('orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_items/<int:order_item_id>/', views.get_order_item, name='get_order_item'),
    path('order_items/<int:order_item_id>/delete/', views.delete_order_item, name='delete_order_item'),
    path('create_order_item/', views.create_order_item, name='create_order_item'),

    path('create_orders_edited/', views.create_orders_edited, name='create_orders_edited'),

    path('create_order_timeline/', views.create_order_timeline, name='create_order_timeline'),

    path('create_order_online_payment/', views.create_order_online_payment, name='create_order_online_payment'),

    path('reviews/', views.get_reviews, name='get_reviews'),
    path('reviews/create/', views.create_review, name='create_review'),
]
