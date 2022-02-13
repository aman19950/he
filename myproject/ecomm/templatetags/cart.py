from atexit import register
from math import prod
from django import template

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
