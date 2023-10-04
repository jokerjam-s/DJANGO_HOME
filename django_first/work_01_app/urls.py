from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients_list, name='clients'),
    path('clients/orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('clients/products/<int:client_id>/<int:days_history>', views.client_prods, name='client_prods'),
]
