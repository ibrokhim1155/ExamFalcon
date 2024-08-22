from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user import auth_views

urlpatterns = [
    path('logout/', auth_views.user_logout, name='logout'),
    path('login/', auth_views.user_login, name='login'),
    path('register/', auth_views.register, name='register'),
    path('send-email/', auth_views.SendingEmail.as_view(), name='sending_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
