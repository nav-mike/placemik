from django.views.generic import ListView
from webapp.models.category import Category
from webapp.models.product import Product


class IndexView(ListView):
    template_name: str = "webapp/products/index.html"
    model = Product
    context_object_name = "products"
    queryset = Product.objects.prefetch_related("category")
    paginate_by: int = 20

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get("category"):
            queryset = queryset.filter(category_id=int(self.request.GET["category"]))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get("category"):
            context["category"] = Category.objects.get(
                pk=int(self.request.GET["category"])
            )

        return context
