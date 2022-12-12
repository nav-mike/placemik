from .index_view import *
from .products import IndexView as ProductsIndexView
from .products import DetailView as ProductsDetailView
from .pages.detail_view import DetailView as PagesDetailView
from .newsletter.create_view import CreateNewsletterView
from .order_item import OrderItemCreateView, OrderItemDeleteView
from .carts import DetailView as CartView
from .reviews.create_view import CreateRewievView
from .orders.form_view import OrderCreateView
from .orders.success_payment_view import SuccessPaymentView
from .orders.fail_payment_view import FailPaymentView
