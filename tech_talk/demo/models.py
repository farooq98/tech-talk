from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


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
    order_date = models.DateTimeField(auto_now_add=True)
    demo_order_date = models.DateTimeField()

    @property
    def total(self) -> float:
        total = 0
        for line in self.order_lines.all():
            total += line.product.price * line.quantity
        return total

    def __str__(self):
        return f"{self.id} - {self.customer_name}"


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_order_lines")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_lines")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} - {self.product.name}"
