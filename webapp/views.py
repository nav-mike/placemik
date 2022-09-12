from typing import Any, Dict
from .models import Category
from django.views import generic


class IndexView(generic.ListView):
    template_name = "webapp/index.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    template_name = "webapp/details.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_object().product_set.all()
        return context
