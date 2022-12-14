# Generated by Django 4.1.3 on 2022-12-01 06:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('contact', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('RECEIVED', 'RECEIVED'), ('SHIPPED', 'SHIPPED'), ('DELIVERED', 'DELIVERED')], default='RECEIVED', max_length=50)),
                ('cod', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.product')),
            ],
        ),
    ]
