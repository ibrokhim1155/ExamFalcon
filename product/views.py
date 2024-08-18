from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from product.models import Product


def product_list(request):
    products = Product.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(products, 3)
    page_obj = paginator.get_page(page)

    context = {
    'products': page_obj,
            }

    return render(request, 'product/product-list.html', context)
