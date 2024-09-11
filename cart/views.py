from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse, HttpResponse


# Create your views here.
@require_POST
def add_to_cart(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        request.session.modified = True
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
        }
        return JsonResponse(context)
    except ValueError as e:
        return JsonResponse({'error': str(e)})


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse('cleaned')


@require_POST
def update_quantity(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    action = request.POST.get('action')
    product = get_object_or_404(Product, id=product_id)
    try:
        if action == 'increase':
            cart.add(product)
        elif action == 'decrease':
            cart.decrease(product)

        context = {
            'new_quantity': cart.get(product.id, 'quantity'),
            'total_price': cart.get_total_price(),
            'item_count': len(cart),
        }
        return JsonResponse(context)

    except ValueError as e:
        return JsonResponse({'error': str(e)})


@require_POST
def remove_product(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    try:
        cart.remove(product)
        context = {
            'total_price': cart.get_total_price(),
            'item_count': len(cart),
        }
        return JsonResponse(context)

    except ValueError as e:
        return JsonResponse({'error': str(e)})
