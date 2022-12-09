from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
import stripe

from webapp.forms import OrderForm
from webapp.models import Order, OrderItem, Product


class OrderCreateView(FormView):
    template_name = "webapp/orders/create.html"
    form_class = OrderForm
    model = Order

    def form_valid(self, form):
        order = form.save()
        cart = self.request.session.get("cart", {})
        products = Product.objects.filter(pk__in=cart)
        for product_id, qty in cart.items():
            product = products.get(pk=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
            )
            order.total_price += qty * product.price
        order.save()
        self.request.session["cart"] = {}
        self.success_url = self.stripe_url_generation(order)
        return super().form_valid(form)

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return (
            super().get(request, *args, **kwargs)
            if self.request.session.get("cart")
            else HttpResponseRedirect(self.request.path_info)
        )

    def stripe_url_generation(self, order: Order) -> str:
        line_items = [
            {
                "quantity": item.quantity,
                "price_data": {
                    "unit_amount": int(item.price) * 100,
                    "currency": "usd",
                    "product_data": {
                        "name": item.product.name,
                        "description": item.product.description,
                        "images": [item.product.image_url],
                    },
                },
            }
            for item in order.order_items.all().prefetch_related("product")
        ]
        session = stripe.checkout.Session.create(
            line_items=line_items,
            payment_method_types=["card"],
            mode="payment",
            success_url=self.request.build_absolute_uri(
                reverse_lazy("webapp:success_payment", kwargs={"pk": order.pk})
            ),
            cancel_url=self.request.build_absolute_uri(reverse_lazy("webapp:index")),
        )
        return session.url
