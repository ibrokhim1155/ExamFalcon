from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'

    def ready(self):
        import product.signals


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
