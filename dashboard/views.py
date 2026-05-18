from django.shortcuts import render

from django.views.generic import CreateView
from app.models import Category, Post
from .forms import AddPostForm, CategoryAddForm

# Create your views here.


# ============================
# ADD CATEGORY VIEW
# ============================
class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'dashboard/add_category.html'


# ==============================
# ADD POST VIEW
# ==============================
class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'dashboard/add_post.html'
