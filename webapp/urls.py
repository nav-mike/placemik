from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products/", views.ProductsIndexView.as_view(), name="products"),
    path(
        "products/<int:pk>", views.ProductsDetailView.as_view(), name="products_detail"
    ),
]
