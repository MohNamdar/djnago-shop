from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView

from shop.models import Product, Category


# Create your views here.
def index(request):
    return HttpResponse("homepage")


class ProductListView(ListView):
    model = Product
    paginate_by = 6
    context_object_name = 'products'
    template_name = 'shop/products_list.html'


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/products_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'shop/products_detail.html', context)
