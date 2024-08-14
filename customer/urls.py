from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from customer import views, auth_views

urlpatterns = [
    path('customer/', views.customer_list, name='customer_list'),
    # path('customer/', views.customer_detail, name='detail'),
    path('customer/new/', views.customer_create, name='customer_create'),
    path('customer/<int:_pk>/', views.customer_detail, name='customer_detail'),
    path('customer/<int:_id>/edit/', views.customer_update, name='customer_update'),
    path('customer/<int:_id>/delete/', views.customer_delete, name='customer_delete'),
    path('logout/', auth_views.user_logout, name='logout'),
    path('login/', auth_views.user_login, name='login'),
    path('register/', auth_views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
