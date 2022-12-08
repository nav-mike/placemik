from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from webapp.forms import OrderForm
from webapp.models import Order, OrderItem, Product


class OrderCreateView(FormView):
    template_name = "webapp/orders/create.html"
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy("webapp:index")

    def form_valid(self, form):
        order = form.save()
        for item in self.request.session.get("cart", []):
            OrderItem.objects.create(
                order=order,
                product=Product.objects.get(pk=item["product_pk"]),
                amount=item["amount"],
            )
        self.request.session["cart"] = []
        return super().form_valid(form)

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return (
            super().get(request, *args, **kwargs)
            if self.request.session.get("cart")
            else HttpResponseRedirect(self.request.path_info)
        )
