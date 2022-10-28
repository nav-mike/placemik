from typing import Any, Dict
from django.views import generic

from webapp.models import CategoryGroup, Product


class IndexView(generic.TemplateView):
    template_name = "webapp/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["deals"] = Product.objects.all()[:12]
        context["seenProducts"] = Product.objects.all()[:5]
        context["categoryGroups"] = CategoryGroup.objects.all().prefetch_related(
            "categories"
        )
        return context
