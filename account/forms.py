from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('شماره تلفن باید بصورت عددی نوشته شود.')
        if ShopUser.objects.exclude(id=self.instance.id).filter(phone=phone).exists():
            raise forms.ValidationError('شماره تلقن از قبل وجود دارد.')
        if not phone.startswith('09'):
            raise forms.ValidationError('شماره تلفن باید با 09 شروع شود.')
        if not len(phone):
            raise forms.ValidationError('شماره تلفن باید 11 رقم باشد.')

        return phone


class ShopUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'address', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('شماره تلفن باید بصورت عددی نوشته شود.')
        if ShopUser.objects.exclude(id=self.instance.id).filter(phone=phone).exists():
            raise forms.ValidationError('شماره تلقن از قبل وجود دارد.')
        if not phone.startswith('09'):
            raise forms.ValidationError('شماره تلفن باید با 09 شروع شود.')
        if not len(phone):
            raise forms.ValidationError('شماره تلفن باید 11 رقم باشد.')

        return phone
