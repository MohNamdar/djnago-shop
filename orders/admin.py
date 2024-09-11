from django.contrib import admin
from .models import OrderItem, Order


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'phone', 'address', 'postal_code', 'province', 'city', 'paid', 'created_at',
        'updated_at')

    list_filter = ('paid', 'created_at', 'updated_at')
    inlines = (OrderItemInline,)
