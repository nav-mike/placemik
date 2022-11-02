from django.views.generic import ListView
from webapp.models.product import Product


class IndexView(ListView):
    template_name: str = "webapp/products/index.html"
    model = Product
    context_object_name = "products"
    queryset = Product.objects.prefetch_related("category")
    paginate_by: int = 20
