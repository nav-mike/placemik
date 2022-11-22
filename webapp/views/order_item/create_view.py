from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from webapp.models import OrderItem


class OrderItemCreateView(CreateView):
    model = OrderItem
    fields = ["product"]
    success_url = "/"

    def get(self, _request, *_args, **_kwargs):
        return HttpResponseRedirect("/")

    def post(self, request, *_args, **_kwargs):
        return self.form_valid(request)

    def form_valid(self, _form: BaseModelForm) -> HttpResponse:
        product_id = self.request.POST.get("product_id")
        cart = self.request.session.get("cart", {})
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        self.request.session["cart"] = cart

        return HttpResponseRedirect(self.request.path_info)
