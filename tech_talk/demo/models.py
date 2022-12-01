from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)


class Order(models.Model):

    RECEIVED = "RECEIVED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"

    STATUS_CHOICES = (
        (RECEIVED, RECEIVED),
        (SHIPPED, SHIPPED),
        (DELIVERED, DELIVERED),
    )

    customer_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=RECEIVED)
    cod = models.BooleanField(default=False)


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
