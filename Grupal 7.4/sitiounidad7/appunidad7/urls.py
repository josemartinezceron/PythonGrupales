from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('welcome/', views.welcome, name='welcome'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('productos/', views.gestion_productos, name='gestion_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('pedidos/', views.gestion_pedidos, name='gestion_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/agregar/producto', views.agregar_pedido_producto, name='agregar_pedido_producto'),
    path('pedidos/ver/<int:pedido_id>/', views.ver_pedido, name='ver_pedido'),
    path('pedidos/editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('pedidosweb/', views.historial_pedido_web, name='historial_pedidos_web'),
    path('pedidosweb/agregar/', views.agregar_pedido, name='agregar_pedido_web'),
    path('pedidosweb/ver/<int:pedido_id>/', views.ver_pedido, name='ver_pedido_web'),
    path('pedidosweb/editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido_web'),
    path('pedidosweb/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido_web'),
]
