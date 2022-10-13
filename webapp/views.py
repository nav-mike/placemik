from typing import Any, Dict
from .models import Category, Product
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "webapp/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["deals"] = Product.objects.all()[:12]
        context["seenProducts"] = Product.objects.all()[:5]
        return context


class DetailView(generic.DetailView):
    model = Category
    template_name = "webapp/details.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_object().product_set.all()
        return context
