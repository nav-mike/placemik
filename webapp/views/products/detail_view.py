from django.views.generic import DetailView
from webapp.models.product import Product


class DetailView(DetailView):
    template_name: str = "webapp/products/detail.html"
    model = Product
    context_object_name = "product"
    queryset = Product.objects.prefetch_related("reviews")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["see_also"] = Product.objects.all()[:5]
        return context
