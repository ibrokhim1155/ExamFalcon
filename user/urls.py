from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import auth_views

urlpatterns = [
    path('logout/', auth_views.user_logout, name='logout'),
    path('login/', auth_views.user_login, name='login'),
    path('register/', auth_views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

