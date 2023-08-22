from django.urls import path
from . import views 


urlpatterns = [
    # URL patterns for the categories_view
    path('categories/', views.categories_view, name='categories_list'),  # GET
    path('categories/create/', views.categories_view, name='create_category'),  # POST
    path('categories/<int:pk>/', views.categories_view, name='update_delete_category'),  # PUT, DELETE

    # URL pattern for the update_outlet_categories_view
    path('update_outlets/', views.update_outlet_categories_view, name='update_outlets'),
]
