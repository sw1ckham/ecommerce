from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """A view that renders the card contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quanity of the specific product to the cart"""
    quanity = int(request.POST.get('quanity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quanity
    else:
        cart[id] = cart.get(id, quanity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """ Adjust the quanity of the specified product to the specified ammount"""
    quanity = int(request.POST.get('quanity'))
    cart = request.session.get('cart', {})

    if quanity > 0:
        cart[id] = quanity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))