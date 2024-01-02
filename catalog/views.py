from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return [name, phone, message]
    return render(request, 'catalog/contact.html')
