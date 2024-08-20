from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q
from django.core.paginator import Paginator

class CustomerListView(View):
    def get(self, request, *args, **kwargs):
        filter_val = request.GET.get('filter', '')
        search_query = request.GET.get('search')

        customers = Customer.objects.all()

        if filter_val:
            customers = customers.order_by('-created_at')
        if search_query:
            customers = customers.filter(Q(first_name__icontains=search_query) |
                                         Q(last_name__icontains=search_query) |
                                         Q(email__icontains=search_query))

        paginator = Paginator(customers, 6)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        context = {'customers': page_obj}
        return render(request, 'customer/customer-list.html', context)


class CustomerCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CustomerForm()
        return render(request, 'customer/customer_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your customer has been created!')
            return redirect('customer_list')
        else:
            messages.error(request, 'Something went wrong!')
            return render(request, 'customer/customer_form.html', {'form': form})


class CustomerDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        search_query = request.GET.get('search')
        if search_query:
            customers = Customer.objects.filter(Q(first_name__icontains=search_query) |
                                                Q(last_name__icontains=search_query) |
                                                Q(email__icontains=search_query))
            return render(request, 'customer/customer-list.html', {'customers': customers})

        customer = get_object_or_404(Customer, slug=slug)
        return render(request, 'customer/detail.html', {'customer': customer})


class CustomerUpdateView(View):
    def get(self, request, slug, *args, **kwargs):
        customer = get_object_or_404(Customer, slug=slug)
        form = CustomerForm(instance=customer)
        return render(request, 'customer/customer_form.html', {'form': form})

    def post(self, request, slug, *args, **kwargs):
        customer = get_object_or_404(Customer, slug=slug)
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your customer has been updated!')
            return redirect('customer_detail', slug=slug)
        else:
            messages.error(request, 'Something went wrong!')
            return render(request, 'customer/customer_form.html', {'form': form})


class CustomerDeleteView(View):
    def post(self, request, slug, *args, **kwargs):
        customer = get_object_or_404(Customer, slug=slug)
        customer.delete()
        messages.success(request, 'Your customer has been deleted!')
        return redirect('customer_list')
