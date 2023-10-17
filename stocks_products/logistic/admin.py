from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]
