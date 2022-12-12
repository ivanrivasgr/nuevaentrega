from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('Producto/', views.producto,name='Producto'),
    path('ProductoApi/', views.productoApi),
    path('busquedaproducto/', views.buscarproducto),
    path('buscar/', views.buscar),
    path('Vendedor/', views.vendedor,name='Vendedor'),
    path('busquedavendedor/', views.buscarvendedor),
    path('buscar1/', views.buscar1),
    path('VendedorApi/', views.vendedorApi),
    path('Cliente/', views.cliente,name='Cliente'),
    path('ClienteApi/', views.clienteApi),
    path('leerProductos/', views.leer_productos),
    path('crearProducto/', views.crear_producto),
    path('editarProducto/', views.editar_producto),
    path('eliminarProducto/', views.eliminar_producto),
    path('producto/list/', views.ProductosList.as_view(),name='List'),
    path("producto/create/", views.ProductosCreate.as_view(),name='New'),
    path("producto/edit/<pk>", views.ProductosEdit.as_view(),name='Edit'),    
    path("producto/detail/<pk>", views.ProductosDetail.as_view(),name='Detail'),
    path("producto/delete/<pk>", views.ProductosDelete.as_view(),name='Delete'),
]
