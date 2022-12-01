from django.contrib import admin
from .models import Product, Order, OrderLine


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class OrderLineAdmin(admin.StackedInline):
    model = OrderLine
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineAdmin]
    list_display = ["id", "customer_name", "total", "contact", "email", "status", "cod"]
    list_editable = ["status", "cod"]
    list_filter = ["status", "cod"]
    date_hierarchy = "demo_order_date"


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderLine)
