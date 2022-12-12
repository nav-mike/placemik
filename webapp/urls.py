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
    path("reviews/", views.CreateRewievView.as_view(), name="reviews_create"),
    path("order_item/", views.OrderItemCreateView.as_view(), name="order_item_create"),
    path(
        "order_item/<int:pk>/delete",
        views.OrderItemDeleteView.as_view(),
        name="order_item_delete",
    ),
    path("cart/", views.CartView.as_view(), name="cart_detail"),
    path("order/", views.OrderCreateView.as_view(), name="order_create"),
    path(
        "success/<uuid:pk>", views.SuccessPaymentView.as_view(), name="success_payment"
    ),
    path("fail/<uuid:pk>", views.FailPaymentView.as_view(), name="fail_payment"),
]
