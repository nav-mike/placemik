from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Category

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, "webapp/index.html", {"categories": categories})


def detail(request: HttpRequest, product_id: int) -> HttpResponse:
    return HttpResponse("You're looking at product %s." % product_id)
