# billing/urls.py

from django.urls import path, include

urlpatterns = [
    path('subscriptions/', include('billing.subscriptions.urls')),  # Include subscriptions URLs
]
