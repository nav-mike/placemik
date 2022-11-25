from django.views.generic import TemplateView


class DetailView(TemplateView):
    template_name: str = "webapp/carts/detail.html"
