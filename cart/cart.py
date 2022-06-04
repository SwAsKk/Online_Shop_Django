from django.conf import settings

from main.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID, None)
        if cart is None:
            cart = {}
        self.cart = cart
        self.save()

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price)
            }
        else:
            if override_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        products = Product.objects.filter(id__in=self.cart.keys())

        for product in products:
            item = self.cart[str(product.id)]
            yield {
                'product': product,
                'price': product.price,
                'quantity': item['quantity'],
                'cost': product.price * int(item['quantity'])
            }

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum([item['cost'] for item in self])

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
