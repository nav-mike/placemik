from typing import List
from django.views.generic.edit import CreateView

from webapp.models.newsletter import Newsletter


class CreateNewsletterView(CreateView):
    http_method_names: List[str] = ["post"]
    model = Newsletter
    fields = ["email"]

    def get_success_url(self) -> str:
        return "/"
