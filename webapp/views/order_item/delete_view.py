from typing import Any, Optional
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from webapp.models import OrderItem


class OrderItemDeleteView(DeleteView):
    model = OrderItem
    success_url: Optional[str] = reverse_lazy("webapp:cart_detail")

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        product_id = self.request.POST.get("product_id")
        cart = self.request.session.get("cart", {})
        if product_id in cart:
            if cart[product_id] > 1:
                cart[product_id] -= 1
            else:
                del cart[product_id]

        self.request.session["cart"] = cart
        return HttpResponseRedirect(self.success_url)
