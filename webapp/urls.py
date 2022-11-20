from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products/", views.ProductsIndexView.as_view(), name="products"),
    path(
        "products/<int:pk>", views.ProductsDetailView.as_view(), name="products_detail"
    ),
    path("pages/<str:slug>", views.PagesDetailView.as_view(), name="pages_detail"),
    path("newsletter/", views.CreateNewsletterView.as_view(), name="newsletter_create"),
]
