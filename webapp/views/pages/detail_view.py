from django.views.generic import DetailView
from webapp.models import Page


class DetailView(DetailView):
    template_name: str = "webapp/pages/detail.html"
    model = Page
    context_object_name = "page"
