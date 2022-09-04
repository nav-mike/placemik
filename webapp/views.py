from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the placemik index.")


def detail(request: HttpRequest, product_id: int) -> HttpResponse:
    return HttpResponse("You're looking at product %s." % product_id)
