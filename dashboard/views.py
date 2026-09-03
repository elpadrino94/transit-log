from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count

from django.views.generic import CreateView, DeleteView, TemplateView, ListView, UpdateView
from app.models import Category, Post
from .forms import AddPostForm, CategoryAddForm
from django.utils import timezone



class DashboardView(TemplateView):
    template_name = 'dash/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['published_count'] = Post.objects.filter(status='published', published_at__lte=now).count()
        return context


# ============================
# POSTS LIST VIEW
# ============================
class PostsListView(ListView):
    model = Post
    template_name = 'dash/post_list.html'
    context_object_name = 'posts' 
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['total_articles'] = Post.objects.count()
        context['published_count'] = Post.objects.filter(status='published', published_at__lte=now).count()
        context['scheduled_count'] = Post.objects.filter(status='published', published_at__gt=now).count()
        context['drafts_count'] = Post.objects.filter(status='draft').count()
        return context


# ============================
# ADD CATEGORY VIEW
# ============================
class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'dash/add_category.html'
    success_url = reverse_lazy('categories-list')

# ==============================
# ADD POST VIEW
# ==============================
class AddPostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'dash/add_post.html'
    success_url = (reverse_lazy('posts-list'))

    # Vérifie si l'utilisateur connecté est bien un administrateur
    def test_func(self):
        return (
            self.request.user.is_authenticated
            and getattr(self.request.user, 'role', None) == 'admin'
        )

    #  Assigne l'admin connecté comme auteur avant d'enregistrer en BDD
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListCategoriesView(ListView):
    template_name = 'dash/list_category.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_queryset(self):
        return Category.objects.annotate(article_count=Count('posts'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_categories'] = Category.objects.count()
        return context

#===========================================
# GESTION DES ACTIONS BOUTONS DE CATEGORIES
#===========================================
class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'dash/add_category.html'
    success_url = reverse_lazy('categories-list')

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and getattr(self.request.user, 'role', None) == 'admin'
        )

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'dash/category_confirm_delete.html'
    success_url = reverse_lazy('categories-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and getattr(self.request.user, 'role', None) == 'admin'
        )

#===========================================
# GESTION DES ACTIONS BOUTONS DES ARTICLES
#===========================================
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'dash/add_post.html'
    success_url = reverse_lazy('posts-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and getattr(self.request.user, 'role', None) == 'admin'
        )

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'dash/post_confirm_delete.html'
    success_url = reverse_lazy('posts-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and getattr(self.request.user, 'role', None) == 'admin'
        )


