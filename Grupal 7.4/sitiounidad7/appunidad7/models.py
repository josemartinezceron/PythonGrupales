from django.db import models
from django.contrib.auth.models import User
import uuid

# Modelo para los productos
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default='Valor predeterminado')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.CharField(max_length=250, default='url')

    def __str__(self):
        return self.nombre

# Modelo para los pedidos
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_entrega = models.CharField(max_length=200)
    forma_pago = models.CharField(max_length=100)
    numero_pedido = models.CharField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.numero_pedido

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    cantidad = models.PositiveIntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_subtotal(self):
        self.subtotal = self.cantidad * self.precio_unitario
        self.save()
# Modelo para el seguimiento de los pedidos
class SeguimientoPedido(models.Model):
    ESTADOS_PEDIDO = (
        ('pendiente', 'Pendiente'),
        ('preparacion', 'En preparación'),
        ('despacho', 'En despacho'),
        ('entregado', 'Entregado'),
    )
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.pedido.numero_pedido} - {self.estado}"

