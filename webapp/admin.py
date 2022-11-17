from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Product, CategoryGroup, Order, OrderItem, Ad, Page


class CategoryGroupResource(resources.ModelResource):
    class Meta:
        model = CategoryGroup


class CategoryGroupAdmin(ImportExportModelAdmin):
    resource_class = CategoryGroupResource


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order


class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource


class OrderItemResource(resources.ModelResource):
    class Meta:
        model = OrderItem


class OrderItemAdmin(ImportExportModelAdmin):
    resource_class = OrderItemResource


class AdResource(resources.ModelResource):
    class Meta:
        model = Ad


class AdAdmin(ImportExportModelAdmin):
    resource_class = AdResource


class PageResource(resources.ModelResource):
    class Meta:
        model = Page


class PageAdmin(ImportExportModelAdmin):
    resource_class = PageResource


admin.site.register(CategoryGroup, CategoryGroupAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Ad, AdAdmin)
