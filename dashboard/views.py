from django.shortcuts import render

from django.views.generic import CreateView, TemplateView
from app.models import Category, Post
from .forms import AddPostForm, CategoryAddForm

# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dash/dashboard.html'


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
class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'dash/add_post.html'
