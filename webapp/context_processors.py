from ctypes import Array
from django.http import HttpRequest
from webapp.models import CategoryGroup
from theme.forms import NewsletterForm, TextSearchForm
from webapp.models import OrderItem, Product


def categories(request):
    return {
        "categoryGroups": CategoryGroup.objects.all().prefetch_related("categories"),
        "newsletterForm": NewsletterForm(),
        "textSearchForm": TextSearchForm(initial=request.GET),
        "cart": cart(request),
    }


def cart(request: HttpRequest) -> Array[OrderItem]:
    cart = request.session.get("cart", {})

    if not cart:
        return []

    result = []
    products = Product.objects.filter(pk__in=list(cart.keys()))

    for key, value in cart.items():
        product = products.get(pk=key)
        result.append(
            OrderItem(
                product=product,
                quantity=value,
                price=product.price * value,
            )
        )

    return result
