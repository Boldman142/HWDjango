from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Захади дарагой'
    }
    return render(request, 'catalog/index.html', context)


def product(request, pk):
    prod_type = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Все что есть из {prod_type.name}'
    }
    return render(request, 'catalog/product.html', context)


def contact_view(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
        return [name, phone, message]
    return render(request, 'catalog/contact.html', context)
