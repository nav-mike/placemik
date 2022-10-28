from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products/", views.ProductsIndexView.as_view(), name="products"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
