from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
from .models import Producto, Pedido, PedidoProducto
from .forms import ProductoForm, PedidoProductoForm, PedidoForm
# Create your views here.
def home(request):
    return render(request, 'index.html' )

def welcome(request):
    return render(request, 'welcome.html')

def catalogo(request):
    # Obtener todos los productos de la base de datos
    productos = Producto.objects.all()
    # Renderizar la plantilla del catálogo y pasarle los productos como contexto
    return render(request, 'catalogo.html', {'productos': productos})

def register(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('welcome')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Password not match'})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect '
                })
        else:
            login(request, user)
            return redirect('welcome')

def signout(request):
    logout(request)
    return redirect('home')

def gestion_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'gestion_pedidos.html', {'pedidos': pedidos})

def ver_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'ver_pedido.html', {'pedido': pedido})

def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestion_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'agregar_pedido.html', {'form': form})

def agregar_producto_pedido(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))

        producto = Producto.objects.get(id=producto_id)
        precio_unitario = producto.precio

        pedido_id = request.POST.get('pedido')
        pedido = Pedido.objects.get(id=pedido_id)  # Reemplaza 'pedido_id' con el ID correcto

        pedido_producto = PedidoProducto(
            pedido=pedido, 
            producto=producto, 
            cantidad=cantidad, 
            precio_unitario=precio_unitario
        )
        pedido_producto.calcular_subtotal()
        pedido_producto.save()

        # Otras acciones que desees realizar después de agregar el producto al pedido

        productos_disponibles = Producto.objects.all()
    return render(request, 'agregar_producto_pedido.html', {'productos_disponibles': productos_disponibles})

def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('gestion_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form})

def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('gestion_pedidos')
    return render(request, 'gestion_pedidos.html', {'pedido': pedido})

def gestion_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestion_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('gestion_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('gestion_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def historial_pedido_web(request):
    return render(request, 'historial_pedido_web.html')

