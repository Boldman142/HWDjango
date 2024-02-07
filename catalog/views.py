from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django import forms


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Захади дарагой'
    }


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'
    form_class = ProductForm

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:product_update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        # num_true = Version.objects.all().filter(product_id=self.get_object().id)
        # numm = 0
        # for i in num_true:
        #     if i.sign:
        #         numm += 1
        # if numm > 1:
        #     raise forms.ValidationError(f'Увы, не больше одного варианта в наличии') #Как бы сделать, чтобы как клин
        #     # метод в формах, просто не пускал так сделать, а не ронял все
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
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
        #
        # products = Product.objects.all()
        # version_all = Version.object.all().filter(product_id=self.get_object().id)
        # for product in products:
        #     product.active_version = product.versions.filter(is_active=True).first()
        # context_data['products'] = products


        return context_data


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
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
