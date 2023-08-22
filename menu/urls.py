from django.urls import path, include
from . import views

urlpatterns = [
    path('addons/', include('menu.addons.urls')), 
    path('categories/', include('menu.categories.urls')), 
    path('varaints/', include('menu.variants.urls')), 
    path('get/', views.get_view, name='get_view'),
    path('post/', views.post_view, name='post_view'),
    path('put/', views.put_view, name='put_view'),
    path('delete/', views.delete_view, name='delete_view'),
    path('create_combo_items/', views.create_combo_items_link, name='create_combo_items_link'),
    path('delete_combo_items/', views.delete_combo_items_link, name='delete_combo_items_link'),
    path('variant_post/', views.variant_post_view, name='variant_post_view'),
    path('variant_put/', views.variant_put_view, name='variant_put_view'),
    path('variant_delete/', views.variant_delete_view, name='variant_delete_view'),
    path('item-outlet-link/', views.create_item_outlet_link, name='create_item_outlet_link'),
    path('item-outlet-link/<int:pk>/', views.update_item_outlet_link, name='update_item_outlet_link'),

]
