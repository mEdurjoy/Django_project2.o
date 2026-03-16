from django.contrib import admin

# Register your models here.
from . models import (
    Product,
    # u can add your all model name
)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discount_price', 'description', 'brand', 'catagory', 'product_image']