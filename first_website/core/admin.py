from django.contrib import admin
from core.models import Product, Tag, Review

# Register your models here.

admin.site.register([Tag, Review])

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]

    search_fields = ["title"]
    sortable_by = ["title", "price"]
    list_filter = ["title"]
