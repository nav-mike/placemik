from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from .models import Category

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, "webapp/index.html", {"categories": categories})


def detail(request: HttpRequest, category_id: int) -> HttpResponse:
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        raise Http404("Category does not exist") from e
    return render(request, "webapp/details.html", {"category": category})
