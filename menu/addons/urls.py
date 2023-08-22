from django.urls import path
from .views import (
    category_post_view,
    category_get_view,
    addon_get_view,
    category_put_view,
    delete_view,
    addon_put_view,
    addon_post_view,
    UpdateOutletView,
    create_addon_category_link
)

urlpatterns = [
    path('api/category/', category_post_view, name='category-post'),
    path('api/category/', category_get_view, name='category-get'),
    path('api/addon/', addon_get_view, name='addon-get'),
    path('api/category/<int:pk>/', category_put_view, name='category-put'),
    path('api/delete/', delete_view, name='delete'),
    path('api/addon/', addon_put_view, name='addon-put'),
    path('api/addon/', addon_post_view, name='addon-post'),
    path('api/update_outlet/', UpdateOutletView.as_view(), name='update-outlet'),
    path('create-addon-category-link/', create_addon_category_link, name='create_addon_category_link'),
]
