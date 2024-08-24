from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from product.models import Product, Category, Image, Attribute, AttributeValue, ProductAttribute

# Register Product, Category, and Image with the default admin interface
admin.site.register([Product, Category, Image])

# Define resource classes for import/export
class AttributeResource(resources.ModelResource):
    class Meta:
        model = Attribute
        fields = ('id', 'key', 'created_at')

class AttributeValueResource(resources.ModelResource):
    class Meta:
        model = AttributeValue
        fields = ('id', 'value', 'created_at')

class ProductAttributeResource(resources.ModelResource):
    class Meta:
        model = ProductAttribute
        fields = ('id', 'product', 'attribute', 'value', 'created_at', 'updated_at')

# Base TimestampAdmin class with import/export functionality
class TimestampAdmin(ImportExportModelAdmin):
    list_filter = ('created_at',)
    search_fields = ('value',)

@admin.register(Attribute)
class AttributeAdmin(TimestampAdmin):
    resource_class = AttributeResource
    list_display = ('id', 'key')

@admin.register(AttributeValue)
class AttributeValueAdmin(TimestampAdmin):
    resource_class = AttributeValueResource
    list_display = ('id', 'value')

@admin.register(ProductAttribute)
class ProductAttributeAdmin(TimestampAdmin):
    resource_class = ProductAttributeResource
    list_display = ('id', 'product', 'attribute', 'value', 'created_at', 'updated_at')
    search_fields = ('product__name', 'attribute__key', 'value__value')
    list_filter = ('created_at', 'product')
