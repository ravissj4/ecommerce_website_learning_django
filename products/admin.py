from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_display = ['title', 'price', 'active', 'updated']

    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Product


# Register your models here.
admin.site.register(Product, ProductAdmin)