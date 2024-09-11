from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def get(self, product_id, key):
        try:
            return self.cart[str(product_id)][key]
        except:
            raise ValueError("Invalid Request")

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity,
                                     'price': product.new_price, 'weight': product.weight}
        else:
            if self.cart[product_id]['quantity'] < product.inventory:
                self.cart[product_id]['quantity'] += quantity
            else:
                raise ValueError('بیش از این در انبار موجود نمی باشد')
        self.save()

    def decrease(self, product, quantity=1):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > quantity:
            self.cart[product_id]['quantity'] -= quantity
            self.save()
        else:
            raise ValueError(f'حداقل مقدار مجاز {quantity} است')

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        del self.session['cart']
        self.save()

    def get_post_price(self):
        weight = sum(item['weight'] * item['quantity'] for item in self.cart.values())
        if weight < 1000:
            return 35000
        elif weight < 2000:
            return 50000
        elif weight > 2000:
            return 80000

    def get_total_price(self):
        price = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return price

    def get_total_off(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        off = sum(self.cart[str(product.id)]['quantity'] * product.off for product in products)
        return off

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_dict = self.cart.copy()
        for product in products:
            cart_dict[str(product.id)]['product'] = product

        for item in cart_dict.values():
            yield item

    def save(self):
        self.session.modified = True
