from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user.auth_views import RegisterPage, LoginView, LogoutView
from user.auth_views import SendingEmail, activate_account

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('send-email/', SendingEmail.as_view(), name='send_email'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
