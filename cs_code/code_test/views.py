from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context, loader
from django.db.models import Sum


from .models import *

def index(request):
    # return render(request, 'code_test/index.html')
    return render(request, 'code_test/home.html')

@login_required
def products(request):
    admin = Admin.objects.get(user_id=request.user.id)
    product_list = Product.objects.filter(admin_id=admin.id)
    template = loader.get_template('code_test/product_list.html')
    # return render(request, 'code_test/product_list.html')
    context = {
        'product_list': product_list,
        'admin': admin,
    }
    return HttpResponse(template.render(context, request))


@login_required
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    template = loader.get_template('code_test/product_detail.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))


@login_required
def productedit(request, product_id):
    product = Product.objects.get(id=product_id)
    template = loader.get_template('code_test/product_edit.html')
    form = ProductForm(instance=product)
    context = {
        'product': product,
        'form': form,
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        form.save()
        if form.is_valid():
            product = Product.objects.get(id=product_id)
            context['product'] = product
            template = loader.get_template('code_test/product_detail.html')
            return redirect('product_detail', product_id)
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
 
    return HttpResponse(template.render(context, request))


@login_required
def createproduct(request):
    admin = Admin.objects.get(user_id=request.user.id)
    template = loader.get_template('code_test/product_create.html')
    form = ProductForm(initial={'admin': admin.id})
    context = {
        'form': form,
    }
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        form = ProductForm(request.POST)
        if form.is_valid():
            form.cleaned_data['admin_id'] = admin.id
            product = form.save()
            return redirect('product_detail', product.id)

    return HttpResponse(template.render(context, request))


@login_required
def inventory(request):
    admin = Admin.objects.get(user_id=request.user.id)
    product_id = request.GET.get('product_id', None)
    sku = request.GET.get('sku', None)
    max_qty = request.GET.get('max_qty', None)
    filter = request.GET.get('filter', None)
    reset = request.GET.get('reset', None)
    inventory = Inventory.objects.filter(product__admin=admin.id)
    
    if filter:
        if product_id:
            inventory = inventory.filter(product_id=product_id)
        if sku:
            inventory = inventory.filter(sku=sku)
        if max_qty:
            inventory = inventory.filter(quantity__lte=max_qty)
    else:
        product_id = ''
        sku = ''
        max_qty = ''
    inv_sum = inventory.aggregate(Sum('quantity'))
    template = loader.get_template('code_test/inventory.html')
    context = {
        'inventory': inventory,
        'inv_sum': inv_sum['quantity__sum'],
        'admin': admin,
    }
    if product_id:
        context['filter_product_id'] = product_id
    if sku:
        context['filter_sku'] = sku
    if max_qty:
        context['filter_max_qty'] = max_qty
    return HttpResponse(template.render(context, request))