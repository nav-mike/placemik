from django.views.generic import DetailView

from webapp.models import Order


class SuccessPaymentView(DetailView):
    template_name = "webapp/orders/success_payment.html"
    model = Order
