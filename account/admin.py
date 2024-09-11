from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ShopUser
from .forms import ShopUserCreationForm, ShopUserChangeForm


@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):
    model = ShopUser
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm
    ordering = ('phone',)
    list_display = ('phone', 'first_name', 'last_name', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('phone', 'password',)}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'address')}),
        ('دسترسی ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخ ها', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'password1', 'password2',)}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'address',)}),
        ('دسترسی ها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}) ,
    )
