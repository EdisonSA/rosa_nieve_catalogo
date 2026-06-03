from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.db.models import Q
from .carrito import Carrito

def home(request):
    return render(request, 'gestion_rosa_nieve/home.html')

def menu_bar(request):
    categoria_slug = request.GET.get('categoria')
    query = request.GET.get('buscar')
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
        
    if categoria_slug:
        productos = productos.filter(categoria_principal=categoria_slug)

    carrito = Carrito(request)
    request.session["carrito_total"] = carrito.get_total_carrito()

    return render(request, 'gestion_rosa_nieve/menu.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'gestion_rosa_nieve/detalle_producto.html', {'producto': producto})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect(f'/producto/{producto_id}/#seccion-botones')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("menu")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect("menu")

def sumar_unidad(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("menu")

def restar_unidad(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect("menu")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("menu")