from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Products


def catalog(request, category_slug):
    
    page = request.GET.get('page', 1)

    if category_slug == 'all': 
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(object_list= goods, per_page= 3)
    current_page = paginator.page(int(page))


    context = {
        "titel": "Home - catalog",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context=context)



def product(request, product_slug):

    req_product = Products.objects.get(slug=product_slug)

    context = {
        'product': req_product
    }

    return render(request, "goods/product.html", context=context)
