from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import CreateView, TemplateView, ListView
from app.models import Category, Post
from .forms import AddPostForm, CategoryAddForm



class DashboardView(TemplateView):
    template_name = 'dash/dashboard.html'


# ============================
# POSTS LIST VIEW
# ============================
class PostsListView(ListView):
    model = Post
    template_name = 'dash/post_list.html'
    context_object_name = 'posts'


# ============================
# ADD CATEGORY VIEW
# ============================
class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'dash/add_category.html'


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

