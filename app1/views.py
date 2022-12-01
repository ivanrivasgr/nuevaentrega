from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Productos
from app1.models import Vendedores
from app1.models import Clientes
from django.core import serializers



# Create your views here.
def inicio(request):
    return render(request, "app1/inicio.html")  

def Producto(request):
    return render(request, "app1/productos.html")

def ProductoApi(request):
    productos_todos = Producto.objects.all()
    return HttpResponse(serializers.serialize('json',productos_todos))

def Vendedor(request):
    return render(request, "app1/vendedor.html")

def VendedorApi(request):
    vendedores_todos = Vendedor.objects.all()
    return HttpResponse(serializers.serialize('json',vendedores_todos))

def Cliente(request):
    return render(request, "app1/cliente.html")

def ClienteApi(request):
    clientes_todos = Cliente.objects.all()
    return HttpResponse(serializers.serialize('json',clientes_todos))
