from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Productos
from app1.models import Vendedores
from app1.models import Clientes
from django.core import serializers
from app1.forms import ProductoFormulario
from app1.forms import VendedorFormulario
from app1.forms import ClienteFormulario


def buscar(request):
    productos_views = request.GET.get("productos_views") 
    productos_todos = Productos.objects.filter(nombreCompleto=productos_views)
    return render(request,"app1/resultadoproductos.html",{"productos":productos_views,"productos":productos_todos})

def buscar1(request):
    vendedores_views = request.GET.get("vendedores_views")
    vendedores_todos = Vendedores.objects.filter(nombreCompleto=vendedores_views)
    return render(request,"app1/resultadovendedores.html",{"vendedores":vendedores_views,"vendedores":vendedores_todos})

def buscar2(request):
    clientes_views = request.GET.get("clientes_views")
    clientes_todos = Clientes.objects.filter(nombreCompleto=clientes_views)
    return render(request,"app1/resultadoclientes.html",{"clientes":clientes_views,"clientes":clientes_todos})

def buscarproducto(request):
    return render(request, "app1/busquedaproducto.html")  

def buscarvendedor(request):
    return render(request, "app1/busquedavendedor.html")

def buscarcliente(request):
    return render(request, "app1/busquedacliente.html")

# Create your views here.
def inicio(request):
    return render(request, "app1/inicio.html")  

def producto(request):
    if request.method == "POST":
    
            miFormulario = ProductoFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                    informacion = miFormulario.cleaned_data
                    Producto = Productos(nombreCompleto=informacion["nombreCompleto"], Referencia=informacion["Referencia"], fechadecaducidad=informacion["fechadecaducidad"], categoria=informacion["categoria"])
                    Producto.save()
                    return render(request, "app1/inicio.html")
    else:
            miFormulario = ProductoFormulario()

    return render(request, "app1/productos.html",{"miFormulario":miFormulario})

def productoApi(request):
    productos_todos = Productos.objects.all()
    return HttpResponse(serializers.serialize('json',productos_todos))

def vendedor(request):
    if request.method == "POST":
    
            miFormulario = VendedorFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                    informacion = miFormulario.cleaned_data
                    Vendedor = Vendedores(nombreCompleto=informacion["nombreCompleto"], telefono=informacion["telefono"], fechaNac=informacion["fechaNac"])
                    Vendedor.save()
                    return render(request, "app1/inicio.html")
    else:
            miFormulario = VendedorFormulario()

    return render(request, "app1/vendedor.html",{"miFormulario":miFormulario})

def vendedorApi(request):
    vendedores_todos = Vendedores.objects.all()
    return HttpResponse(serializers.serialize('json',vendedores_todos))

def cliente(request):
    if request.method == "POST":
    
            miFormulario = ClienteFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                    informacion = miFormulario.cleaned_data
                    Cliente = Clientes(nombreCompleto=informacion["nombreCompleto"], telefono=informacion["telefono"], fechaNac=informacion["fechaNac"])
                    Cliente.save()
                    return render(request, "app1/inicio.html")
    else:
            miFormulario = ClienteFormulario()
     
    return render(request, "app1/cliente.html",{"miFormulario":miFormulario})

def clienteApi(request):
    clientes_todos = Clientes.objects.all()
    return HttpResponse(serializers.serialize('json',clientes_todos))

#-----------------------------------------

def leer_productos(request):
    productos_all = Productos.objects.all()
    return HttpResponse(serializers.serialize("json",productos_all))

def crear_producto(request):
    producto = Productos(nombreCompleto="ProductosTest",Referencia="0001", fechadecaducidad="0001-01-01", categoria="categoria")
    producto.save()
    return HttpResponse(f'Productos {producto.nombreCompleto} ha sido creado')

def editar_producto(request):
    nombreCompleto_consulta = "ProductoTest"
    Productos.objects.filter(nombreCompleto=nombreCompleto_consulta).update(nombreCompleto="NombrenuevoProductoTest")
    return HttpResponse(f'Productos {nombreCompleto_consulta} ha sido actualizado')

def eliminar_producto(request):
    nombreCompleto_nuevo='NombrenuevoProductoTest'
    producto = Productos.objects.get(nombreCompleto=nombreCompleto_nuevo)
    producto.delete()
    return HttpResponse(f'Productos {nombreCompleto_nuevo} ha sido eliminado')

#-----------------------------------------

def leer_vendedores(request):
    vendedores_all = Vendedores.objects.all()
    return HttpResponse(serializers.serialize("json",vendedores_all))

def crear_vendedor(request):
    vendedor = Vendedores(nombreCompleto="VendedoresTest",telefono="0000001", fechaNac="0001-01-01")
    vendedor.save()
    return HttpResponse(f'Vendedores {vendedor.nombreCompleto} ha sido creado')

def editar_vendedor(request):
    nombreCompleto_consulta = "VendedorTest"
    Vendedores.objects.filter(nombreCompleto=nombreCompleto_consulta).update(nombreCompleto="NombrenuevoVendedorTest")
    return HttpResponse(f'Vendedores {nombreCompleto_consulta} ha sido actualizado')

def eliminar_vendedor(request):
    nombreCompleto_nuevo='NombrenuevoVendedorTest'
    vendedor = Vendedores.objects.get(nombreCompleto=nombreCompleto_nuevo)
    vendedor.delete()
    return HttpResponse(f'Vendedores {nombreCompleto_nuevo} ha sido eliminado')

#-----------------------------------------

def leer_clientes(request):
    clientes_all = Clientes.objects.all()
    return HttpResponse(serializers.serialize("json",clientes_all))

def crear_cliente(request):
    cliente = Clientes(nombreCompleto="ClientesTest",telefono="0000001", fechaNac="0001-01-01")
    cliente.save()
    return HttpResponse(f'Clientes {cliente.nombreCompleto} ha sido creado')

def editar_cliente(request):
    nombreCompleto_consulta = "ClienteTest"
    Clientes.objects.filter(nombreCompleto=nombreCompleto_consulta).update(nombreCompleto="NombrenuevoClienteTest")
    return HttpResponse(f'Clientes {nombreCompleto_consulta} ha sido actualizado')

def eliminar_cliente(request):
    nombreCompleto_nuevo='NombrenuevoClienteTest'
    cliente = Clientes.objects.get(nombreCompleto=nombreCompleto_nuevo)
    cliente.delete()
    return HttpResponse(f'Clientes {nombreCompleto_nuevo} ha sido eliminado')



#Hay que hacerlo con cada clase
#-----------------------------------------
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView



class ProductosList(ListView):
    model = Productos
    template = "app1/productos_list.html"

class ProductosCreate(CreateView):
    model = Productos
    fields = ['nombreCompleto','Referencia','fechadecaducidad','categoria']
    success_url = "/app1/producto/list/"

class ProductosEdit(UpdateView):
    model = Productos
    fields = ['nombreCompleto','Referencia','fechadecaducidad','categoria']
    success_url = "/app1/producto/list/"

class VendedoresList(ListView):
    model = Vendedores
    template = "app1/vendedores_list.html"

class VendedoresCreate(CreateView):
    model = Vendedores
    fields = ['nombreCompleto','telefono','fechaNac']
    success_url = "/app1/vendedor/list/"

class VendedoresEdit(UpdateView):
    model = Vendedores
    fields = ['nombreCompleto','telefono','fechaNac']
    success_url = "/app1/vendedor/list/"

class ClientesList(ListView):
    model = Clientes
    template = "app1/clientes_list.html"

class ClientesCreate(CreateView):
    model = Clientes
    fields = ['nombreCompleto','telefono','fechaNac']
    success_url = "/app1/cliente/list/"

class ClientesEdit(UpdateView):
    model = Clientes
    fields = ['nombreCompleto','telefono','fechaNac']
    success_url = "/app1/cliente/list/"

from django.views.generic.detail import DetailView

class ProductosDetail(DetailView):
    model = Productos
    template_name = "app1/productos_detail.html"

class ProductosDelete(DeleteView):
    model = Productos
    fields = '__all__'
    success_url = "/app1/producto/list/"

class VendedoresDetail(DetailView):
    model = Vendedores
    template_name = "app1/vendedores_detail.html"

class VendedoresDelete(DeleteView):
    model = Vendedores
    fields = '__all__'
    success_url = "/app1/vendedor/list/"

class ClientesDetail(DetailView):
    model = Clientes
    template_name = "app1/clientes_detail.html"

class ClientesDelete(DeleteView):
    model = Clientes
    fields = '__all__'
    success_url = "/app1/cliente/list/"