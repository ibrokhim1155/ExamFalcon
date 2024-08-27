from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from customer.views import CustomerListView, CustomerCreateView, CustomerDetailView, CustomerUpdateView, CustomerDeleteView,export_data

urlpatterns = [
    path('customer/export-data/', export_data, name='export_data'),  # Buni oldinga ko'chirish kerak
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/new/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<slug:slug>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/<slug:slug>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<slug:slug>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)