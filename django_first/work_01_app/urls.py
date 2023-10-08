from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients_list, name='clients'),
    path('clients/orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('clients/products/<int:client_id>/<int:days_history>', views.client_prods, name='client_prods'),
    path('products/', views.products_list, name='products'),
    path('products/<slug:show_no_del>', views.products_list, name='products'),
    path('products/delete/', views.product_delete, name='product_delete'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/info/<int:prod_id>', views.product_info, name='product_info'),
    path('products/edit/<int:prod_id>', views.product_edit, name='product_edit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)