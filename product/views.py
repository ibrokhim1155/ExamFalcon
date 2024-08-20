from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from product.models import Product
from product.forms import ProductForm
from django.contrib import messages



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        context = {
            'products': page_obj,
        }
        return render(request, 'product/product-list.html', context)



class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product/product-form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'product/product-form.html', {'form': form})



class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'product/product-detail.html', context)



class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product/product-form.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your product has been updated.')
            return redirect('product-list')
        return render(request, 'product/product-form.html', {'form': form})



class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('product-list')
