
from django.contrib import auth,messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import authforuser,register,profile
from products.models import baskets
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method=='POST':
        form=authforuser(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('products:main'))
    else:
        form=authforuser()
    context={
        'form':form
    }
    return render(request,'login.html',context)
def registerfor(request):
    if request.method=='POST':
        formregister=register(data=request.POST)
        if formregister.is_valid():
            formregister.save()
            messages.success(request,'succesfuly register')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        formregister=register()
    context={'form':formregister}
    return render(request,'register.html',context)
@login_required
def profilefor(request):
    if request.method=='POST':
        form=profile(data=request.POST,files=request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form=profile(instance=request.user)

    manybaskets=baskets.objects.filter(user=request.user)
    total_sum=0
    total_quantity=0
    for basket in manybaskets:
        total_quantity+=basket.quantity
        total_sum+=basket.sum()

    context = {'form': form,
               'baskets':manybaskets,
                'total_quantity':total_quantity,
                'total_sum':total_sum}

    return render(request,'profile.html',context)
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:main'))