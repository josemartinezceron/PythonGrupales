from django.contrib import admin
from .models import PedidoProducto, Producto, Pedido, SeguimientoPedido

class TablaAuxiliarAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(PedidoProducto, TablaAuxiliarAdmin)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(SeguimientoPedido)






