from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from blog.models import Blog
from blog.services import send


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'message',)
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.name)
            new_post.save()

        return super().form_valid(form)


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    permission_required = 'blog.change_post'
    fields = ('name', 'message',)
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.name)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог, не понятно зачем'
    }

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(published=True)
    #     return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        # if self.object.count_view > 10:
        #     send(topic='Проверка связи', text='Меня слышно?', to=['mrsamy@rambler.ru', 'kapitan.kub@gmail.com'])
        return self.object


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    permission_required = 'blog.delete_post'
    success_url = reverse_lazy('blog:blog')


@permission_required('blog.change_post')
def change_publish(request, pk):
    post_item = get_object_or_404(Blog, pk=pk)
    if post_item.published:
        post_item.published = False
    else:
        post_item.published = True

    post_item.save()

    return redirect(reverse('blog:blog'))
