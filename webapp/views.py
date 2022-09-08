from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
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
