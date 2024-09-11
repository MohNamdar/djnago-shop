from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=255, verbose_name='نام محصول')
    cover = models.ImageField(upload_to='shop/product_images/%Y/%m/', blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(verbose_name='توضیحات')
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت محصول')
    off = models.PositiveIntegerField(default=0, verbose_name='تخفیف', blank=True, null=True)
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن محصول')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف', blank=True, null=True)
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = jmodels.jDateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ویژگی')
    value = models.CharField(max_length=255, verbose_name='مقدار ویژگی')
    product = models.ForeignKey(Product, related_name='features', verbose_name='محصول',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.value}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name='محصول')
    file = models.ImageField(upload_to='shop/product_images/%Y/%m/')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded']
        indexes = [
            models.Index(fields=['-uploaded']),
        ]

        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
