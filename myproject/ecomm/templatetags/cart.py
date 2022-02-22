from django import template
from sqlalchemy import true

register = template.Library()


@register.filter(name='isexistincart')
def isexistincart(product, cart):

    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name="cartquantity")
def cartquantity(product, cart):

    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name="total_price")
def total_price(product, cart):
    return product.price * cartquantity(product, cart)


@register.filter(name="total_cart_price")
def total_cart_price(product, cart):
    sum = 0
    for p in product:
        sum += total_price(p, cart)
    return sum


@register.filter(name="currency")
def currency(num):
    return "$"+str(num)


@register.filter(name="multiplyprice")
def multiplyprice(num, num1):
    return num * num1
