from django.views.generic import DetailView
from webapp.forms import ReviewForm
from webapp.models.product import Product
from webapp.models import Ad


class DetailView(DetailView):
    template_name: str = "webapp/products/detail.html"
    model = Product
    context_object_name = "product"
    queryset = Product.objects.prefetch_related("reviews", "order_items")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["see_also"] = Product.objects.filter(
            category_id=context["product"].category_id
        ).exclude(id=int(self.kwargs["pk"]))[:5]
        context["ads"] = Ad.objects.order_by("?")[:4]
        context["review_form"] = ReviewForm(
            initial={"product": self.kwargs["pk"], "rating": 5}
        )
        return context
