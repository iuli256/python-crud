from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from restaurants.models import NutritionalType, Product, NutritionalValues
from restaurants.forms import ProductForm, NutritionalValuesForm


def index(request):
    lists = {}
    return render(request, 'home.html', {'docs': lists})


# below is the Class Based View version
class NutritionalTypeList(LoginRequiredMixin, ListView):
    login_url = '/cms/login'
    redirect_field_name = 'next'
    model = NutritionalType


class NutritionalTypeView(LoginRequiredMixin, DetailView):
    login_url = '/cms/login'
    redirect_field_name = 'next'
    model = NutritionalType


class NutritionalTypeCreate(LoginRequiredMixin, CreateView):
    login_url = '/cms/login'
    redirect_field_name = 'next'
    model = NutritionalType
    fields = ['name', 'unit']
    success_url = reverse_lazy('nutritional_information_list')


class NutritionalTypeUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/cms/login'
    redirect_field_name = 'next'
    model = NutritionalType
    fields = ['name', 'unit']
    success_url = reverse_lazy('nutritional_information_list')


class NutritionalTypeDelete(LoginRequiredMixin, DeleteView):
    login_url = '/cms/login'
    redirect_field_name = 'next'
    model = NutritionalType
    success_url = reverse_lazy('nutritional_information_list')


# bellow is the Function Based View version
@login_required(login_url='login')
def product_list(request, template_name='products/product_list.html'):
    product_name = None
    status = None
    if request.method == 'POST':
        product_name = request.POST.get('product','')

        status = request.POST.get('status','')
        if status == 'ACTIVE' or status == 'INACTIVE':
            product = Product.objects.filter(name__contains=product_name).filter(status=status)
        else:
            product = Product.objects.filter(name__contains=product_name)
    else:
        product = Product.objects.all()
    data = {}
    lstProducts = []
    for p in product:
        pr = {}
        pr['name'] = p.name
        pr['description'] = p.description
        pr['id'] = p.id
        pr['status'] = p.status
        try:
            nv = NutritionalValues.objects.filter(product=p)
        except NutritionalValues.DoesNotExist:
            nv = None
        pr['nutritionalvalues'] = nv
        lstProducts.append(pr)
    data['object_list'] = lstProducts
    data['product_name'] = product_name
    data['status'] = status
    return render(request, template_name, data)


@login_required(login_url='login')
def product_view(request, pk, template_name='products/product_detail.html'):
    product = get_object_or_404(Product, pk=pk)
    return render(request, template_name, {'object':product})


@login_required(login_url='login')
def product_create(request, template_name='products/product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})


@login_required(login_url='login')
def product_update(request, pk, template_name='products/product_form.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})


@login_required(login_url='login')
def product_delete(request, pk, template_name='products/product_confirm_delete.html'):
    product = get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, template_name, {'object':product})


@login_required(login_url='login')
def nutritional_values_create(request, pId=None, template_name='nutritional_values/nutritional_value_form.html'):
    product = get_object_or_404(Product, pk=pId)
    form = NutritionalValuesForm(request.POST or None, initial={'product': product})
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})


@login_required(login_url='login')
def nutritional_values_update(request, pk, template_name='nutritional_values/nutritional_value_form.html'):
    product = get_object_or_404(NutritionalValues, pk=pk)
    form = NutritionalValuesForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})


@login_required(login_url='login')
def nutritional_values_delete(request, pk, template_name='nutritional_values/nutritional_value_confirm_delete.html'):
    product = get_object_or_404(NutritionalValues, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, template_name, {'object':product})
