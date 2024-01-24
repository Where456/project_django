from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.models import Product, Post


class ProductsListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


@csrf_exempt
def contacts(request):
    """
    Handle contact form submission.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


@method_decorator(csrf_exempt, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image')
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')
    template_name = 'post_form.html'

    def form_valid(self, form):
        """
        Set additional fields when the form is valid.
        """
        form.instance.creation_date = timezone.now()
        form.instance.views_count = 0
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        """
        Update views_count when displaying the post.
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        """
        Filter posts to show only published ones.
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


# views.py
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    template_name = 'post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})



class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def get_context_data(self, **kwargs):
        """
        Add custom title for post deletion.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление поста'
        return context
