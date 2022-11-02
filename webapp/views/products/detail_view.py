from django.views.generic import DetailView
from webapp.models.product import Product


class DetailView(DetailView):
    template_name: str = "webapp/products/detail.html"
    model = Product
    context_object_name = "product"
