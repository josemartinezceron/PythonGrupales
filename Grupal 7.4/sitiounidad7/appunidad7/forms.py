from django import forms
from .models import Producto, PedidoProducto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'direccion_entrega', 'forma_pago', 'numero_pedido']

class PedidoProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pedido_id = kwargs.pop('pedido_id', None)
        self.pedido_id = pedido_id
        super().__init__(*args, **kwargs)

    class Meta:
        model = PedidoProducto
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']