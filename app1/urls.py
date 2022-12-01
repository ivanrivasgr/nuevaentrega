from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('Producto/', views.Producto,name='Producto'),
    path('ProductoApi/', views.ProductoApi),
    path('Vendedor/', views.Vendedor,name='Vendedor'),
    path('VendedorApi/', views.VendedorApi),
    path('Cliente/', views.Cliente,name='Cliente'),
    path('ClienteApi/', views.ClienteApi),
]
