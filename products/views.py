from django.shortcuts import render,HttpResponseRedirect
from .models import productsmodel,baskets,category
from django.core.paginator import Paginator
def main(request):
    return render(request,'index.html',context={'quary':1>2})
def products(request,category_id=None,page=1):

    context = {
    'category': category.objects.all(),
    }
    if category_id:
         products=productsmodel.objects.filter(category_id=category_id)
    else:
        products=productsmodel.objects.all()
    paginator=Paginator(products,2)
    products_paginator=paginator.page(page)
    context.update({'products':products_paginator})
    return render(request,'products.html',context)
def basket_add(request,product_id):
    product=productsmodel.objects.get(id=product_id)
    basket=baskets.objects.filter(user=request.user,product=product)
    if not basket.exists():
        baskets.objects.create(user=request.user,product=product,quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        it_basket=basket.first()
        it_basket.quantity+=1
        it_basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
