from decimal import Decimal

from django.contrib import admin
from .models import Client, Order, Product, OrderProducts


@admin.action(description='Price +5 percent')
def price_add_five(modeladmin, request, queryset):
    for prod in queryset:
        prod.price = prod.price * Decimal(1.05)
        prod.save()


@admin.action(description='Price -5 percent')
def price_sub_five(modeladmin, request, queryset):
    for prod in queryset:
        prod.price = prod.price * Decimal(0.95)
        prod.save()


@admin.action(description="Count to 0")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(prod_count=0)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'cost',)
    ordering = ('-order_date',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'description', 'price', 'prod_count', 'append_date',)
    ordering = ('prod_name', 'price',)
    list_filter = ('prod_name', 'price', 'prod_count',)
    readonly_fields = ('append_date',)
    actions = (reset_quantity, price_sub_five, price_add_five,)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'email', 'password', 'phone', 'address', 'reg_date',)
    ordering = ('client_name',)
    list_filter = ('client_name', 'email', 'phone', 'address',)
    readonly_fields = ('reg_date',)


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
