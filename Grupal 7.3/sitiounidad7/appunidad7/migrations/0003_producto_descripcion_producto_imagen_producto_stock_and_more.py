# Generated by Django 4.2.2 on 2023-07-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appunidad7', '0002_detallepedido_pedido_producto_seguimientopedido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='Valor predeterminado', max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
