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
        elif self.request.GET.get("categoryGroup") and self.request.GET.get("search"):
            if self.request.GET.get("categoryGroup") != "0":
                queryset = queryset.filter(
                    category__group_id=self.request.GET["categoryGroup"],
                    name__icontains=self.request.GET["search"],
                )
            else:
                queryset = queryset.filter(
                    name__icontains=self.request.GET["search"],
                )

        # import pdb

        # pdb.set_trace()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get("category"):
            context["category"] = Category.objects.get(
                pk=int(self.request.GET["category"])
            )
        elif self.request.GET.get("categoryGroup") and self.request.GET.get("search"):
            context["search"] = self.request.GET.get("search")

        return context
