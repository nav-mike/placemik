from typing import List, Type
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from webapp.models.review import Review


class CreateRewievView(CreateView):
    http_method_names: List[str] = ["post"]
    model = Review
    fields = ["rating", "user_name", "product", "text"]

    def get_success_url(self) -> str:
        return reverse("webapp:products_detail", kwargs={"pk": self.object.product_id})
