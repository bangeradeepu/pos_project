from django.urls import path, include
from .views import UsersListView, UsersDetailView, UserCompanyLinkListView, UserCompanyLinkDetailView

urlpatterns = [
    # Users URLs
    path('deliveryExecutives/', include('user.deliveryExecutives.urls')), 
    path('permissions/', include('user.permissions.urls')), 

    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='users-detail'),

    # UserCompanyLink URLs
    path('user-company-links/', UserCompanyLinkListView.as_view(), name='user-company-links-list'),
    path('user-company-links/<int:pk>/', UserCompanyLinkDetailView.as_view(), name='user-company-links-detail'),
]
