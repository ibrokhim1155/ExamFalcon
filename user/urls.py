from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.auth_views import RegisterView, LoginView, LogoutView
from user.views import SendingEmail

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('send-email/', SendingEmail.as_view(), name='sending_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
