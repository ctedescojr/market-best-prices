from django.contrib import admin

from .models import Market, Price, Product


@admin.register(Market)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "marketName", "city", "adress")
    search_fields = ("marketName", "city")


@admin.register(Product)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "productName", "brand", "category")
    search_fields = ("productName", "brand", "category")


@admin.register(Price)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_product", "id_market", "value")
    list_editable = ("id_product",)
    list_per_page = 20
    search_fields = ("id_product",)
