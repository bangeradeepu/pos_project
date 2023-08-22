from django.urls import path
from . import views 

urlpatterns = [
    path('permissions/', views.list_permissions_view, name='list_permissions'),
    path('permissions/add/', views.add_permissions_view, name='add_permissions'),
    path('permissions/delete/', views.delete_permissions_view, name='delete_permissions'),
    path('roles/', views.list_roles_view, name='list_roles'),
    path('roles/add/', views.add_role_view, name='add_role'),
    path('user_roles/', views.list_user_roles_view, name='list_user_roles'),
    path('user_roles/add/', views.add_role_to_user_view, name='add_role_to_user'),
    path('modules/', views.list_modules_view, name='list_modules'),
]
