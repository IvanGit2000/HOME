from django.shortcuts import get_list_or_404, render

from goods.models import Products


def catalog(request, category_slug):
    
    if category_slug == 'all-category': 
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "titel": "Home - catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug):

    req_product = Products.objects.get(slug=product_slug)

    context = {
        'product': req_product
    }

    return render(request, "goods/product.html", context=context)
