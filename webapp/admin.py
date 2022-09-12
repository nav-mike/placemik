from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Product, CategoryGroup


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


admin.site.register(CategoryGroup, CategoryGroupAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
