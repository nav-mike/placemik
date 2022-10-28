from typing import Any, Dict
from django.views.generic import TemplateView

from webapp.models.product import Product


class IndexView(TemplateView):
    template_name: str = "webapp/products/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().prefetch_related("category")
        return context
