# Generated by Django 4.2.2 on 2023-07-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appunidad7', '0006_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
