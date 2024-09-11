from django.db import models

from shop.models import Product


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    address = models.CharField(max_length=255, verbose_name="آدرس پستی")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
    province = models.CharField(max_length=50, verbose_name="استان")
    city = models.CharField(max_length=50, verbose_name="شهر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")
    paid = models.BooleanField(default=False, verbose_name="وضعیت پرداخت")

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at'])]

        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    def __str__(self):
        return f"order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_post_price(self):
        weight = sum(item.get_weight() for item in self.items.all())
        if weight < 1000:
            return 35000
        elif weight < 2000:
            return 50000
        elif weight > 2000:
            return 80000

    def get_final_cost(self):
        return self.get_total_cost() + self.get_post_price()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name="محصول")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت")
    quantity = models.PositiveIntegerField(default=1, verbose_name="مقدار")
    weight = models.PositiveIntegerField(default=0, verbose_name="وزن")

    def __str__(self):
        return str(self.id)

    def get_weight(self):
        return self.weight * self.quantity

    def get_cost(self):
        return self.price * self.quantity
