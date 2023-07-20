# Generated by Django 4.2.2 on 2023-07-17 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appunidad7', '0003_producto_descripcion_producto_imagen_producto_stock_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetallePedido',
            new_name='PedidoProducto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
