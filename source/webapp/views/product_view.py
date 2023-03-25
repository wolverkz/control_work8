from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print('DEBUG:', product.pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/', pk=form.instance.pk)
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    else:
        context = {'product': product}
        return render(request, 'product_delete.html', context)