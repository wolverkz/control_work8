from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Review


def review_list(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    context = {
        'product': product,
        'reviews': reviews
    }
    return render(request, 'review_list.html', context)