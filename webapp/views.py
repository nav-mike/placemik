from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from .models import Category

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, "webapp/index.html", {"categories": categories})


def detail(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=category_id)
    return render(request, "webapp/details.html", {"category": category})
