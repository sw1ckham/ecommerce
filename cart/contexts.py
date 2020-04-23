from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available 
    when rendering every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quanity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quanity * product.price
        product_count += quanity
        cart_items.append({'id':id, 'quanity': quanity, 'product': product})

    return { 'cart_items': cart_items, 'total': total,
    'product_count': product_count }
