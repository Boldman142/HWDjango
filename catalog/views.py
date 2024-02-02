from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Category, Product


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Захади дарагой'
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        prod_type = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = f'Все что есть из {prod_type.name}'

        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog')


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
        context['post'] = {
            'name_user': name,
            'phone_user': phone,
            'message_user': message
        }

    return render(request, 'catalog/contact_list.html', context)
