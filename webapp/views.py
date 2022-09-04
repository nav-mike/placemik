from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Category

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    output = ", ".join([c.name for c in categories])
    return HttpResponse(output)


def detail(request: HttpRequest, product_id: int) -> HttpResponse:
    return HttpResponse("You're looking at product %s." % product_id)
