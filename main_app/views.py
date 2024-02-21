from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.forms import VersionCreateForm, VersionUpdateForm, ProductCreateForm, ProductUpdateForm, PostUpdateForm, \
    PostCreateForm
from main_app.models import Version, Product, Post


class ProductsListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        try:
            version = Version.objects.get(product=product)
        except Version.DoesNotExist:
            version = None

        context['version'] = version
        return context


@csrf_exempt
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'contacts.html')


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.is_banned = any(word in form.cleaned_data['name'].lower() or
                                      word in form.cleaned_data['description'].lower()
                                      for word in ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                                                   'free', 'scam', 'police', 'radar'])
        form.instance.last_modified_date = timezone.now()
        return super().form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'product/product_form.html'

    def get_success_url(self):
        return reverse('product-detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post-list')
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        form.instance.creation_date = timezone.now()
        form.instance.views_count = 0
        form.instance.slug = slugify(form.instance.title)

        form.instance.is_banned = any(word in form.cleaned_data['title'].lower() or
                                      word in form.cleaned_data['content'].lower()
                                      for word in ['casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap',
                                                   'free', 'scam', 'police', 'radar'])

        return super().form_valid(form)


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление поста'
        return context


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class VersionDetailView(DetailView):
    model = Version
    template_name = 'version/version_detail.html'
    context_object_name = 'version'

    def get_object(self, queryset=None):
        version_id = self.kwargs.get('version_id')
        return Version.objects.get(id=version_id)


@method_decorator(login_required(login_url=reverse_lazy('user:login')), name='dispatch')
class VersionCreateView(CreateView):
    model = Version
    form_class = VersionCreateForm
    template_name = 'version/version_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-list')


class VersionUpdateView(UpdateView):
    model = Version
    template_name = 'version/version_form.html'
    form_class = VersionUpdateForm

    def get_success_url(self):
        return reverse('main:version-detail', kwargs={'version_id': self.object.pk})


@login_required
def restricted_access(request):
    return render(request, 'restricted_access.html')
