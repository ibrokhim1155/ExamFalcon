from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CustomerForm
from .models import Customer


def customer_list(request):

    filter = request.GET.get('filter', '')
    customers = Customer.objects.all()
    search = request.GET.get('search')
    if filter:
        customers = customers.all().order_by('-created_at')
    if search:
        customers = Customer.objects.filter(Q(first_name__icontains=search) |
                                            Q(last_name__icontains=search) |
                                            Q(email__icontains=search))
    paginator = Paginator(customers,6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context={'customers':page_obj}


    return render(request, 'customer/customer-list.html', context)


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your customer has been created!')
            return redirect('customer_list')
        messages.error(request, 'Something went wrong!')
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_form.html', {'form': form})


def customer_detail(request, _pk):
    search = request.GET.get('search')
    if search:
        customers = Customer.objects.filter(Q(first_name__icontains=search) |
                                            Q(last_name__icontains=search) |
                                            Q(email__icontains=search))
        return render(request, 'customer/customer-list.html', {'customers': customers})
    customer = get_object_or_404(Customer, pk=_pk)
    return render(request, 'customer/detail.html', {'customer': customer})


def customer_update(request, _id):
    customer = get_object_or_404(Customer, pk=_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your customer has been updated!')
            return redirect('customer_detail', _id)
        messages.error(request, 'Something went wrong!')
        return redirect('customer_detail', _id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer_form.html', {'form': form})


def customer_delete(request, _id):
    customer = get_object_or_404(Customer, pk=_id)
    customer.delete()
    messages.success(request, 'Your customer has been deleted!')
    return redirect('customer_list')
