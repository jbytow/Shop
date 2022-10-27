from django.shortcuts import render

from.models import Products, Category


def index(request):
    categories = Category.objects.all()
    data = {'categories': categories}
    return render(request, 'template.html', data)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    category_product = Products.objects.filter(category=category_user)
    categories = Category.objects.all()
    data = {'category_user': category_user,
            'category_product': category_product,
            'categories': categories}
    return render(request, 'category_product.html', data)


def product(request, id):
    product_user = Products.objects.get(pk=id)
    categories = Category.objects.all()
    data = {'product_user': product_user, 'categories': categories}
    return render(request, 'product.html', data)


pass
