# Generated by Django 4.1.3 on 2022-12-01 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_order_demo_order_date_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='demo.order'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order_lines', to='demo.product'),
        ),
    ]
