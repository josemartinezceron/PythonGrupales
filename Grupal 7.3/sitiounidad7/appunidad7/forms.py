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
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.CheckboxSelectMultiple)
    cantidad = forms.IntegerField()

    class Meta:
        model = PedidoProducto
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario', 'subtotal']