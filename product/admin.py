from django.contrib import admin
from product.models import Product, Category, Image, Attribute, AttributeValue, ProductAttribute

admin.site.register([Product, Category, Image])

class TimestampAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    search_fields = ('value',)

@admin.register(Attribute)
class AttributeAdmin(TimestampAdmin):
    list_display = ('id', 'key')


@admin.register(AttributeValue)
class AttributeValueAdmin(TimestampAdmin):
    list_display = ('id', 'value')

@admin.register(ProductAttribute)
class ProductAttributeAdmin(TimestampAdmin):
    list_display = ('id', 'product', 'attribute', 'value', 'created_at', 'updated_at')
    search_fields = ('product__name', 'attribute__key', 'value__value')
    list_filter = ('created_at', 'product')
