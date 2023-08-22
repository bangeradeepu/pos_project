from django.urls import path
from . import views

urlpatterns = [
    # URLs for Subscription model
    
    path('subscriptions/<int:pk>/', views.SubscriptionDetailView.as_view(), name='subscription-detail'),

    # URLs for ActiveSubscriptions model
    path('active-subscriptions/', views.ActiveSubscriptionsListView.as_view(), name='active-subscriptions-list'),
    path('active-subscriptions/<int:pk>/', views.ActiveSubscriptionsDetailView.as_view(), name='active-subscriptions-detail'),

    # URLs for PaymentDetails model
    path('payment-details/', views.PaymentDetailsListView.as_view(), name='payment-details-list'),
    path('payment-details/<int:pk>/', views.PaymentDetailsDetailView.as_view(), name='payment-details-detail'),

    path('subscriptions/', views.create_subscription, name='create_subscription'),
]
