# Generated by Django 4.2.2 on 2023-07-19 21:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appunidad7', '0004_rename_detallepedido_pedidoproducto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='productos',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='pedidoproducto',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]