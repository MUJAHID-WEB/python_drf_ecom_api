from django.contrib import admin

from .models import Brand, Category, Product
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)