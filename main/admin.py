from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'price', 'rating')
    list_filter = ('type',)
    search_fields = ('title', 'description')
