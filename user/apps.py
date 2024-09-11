from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals