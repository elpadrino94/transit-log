from django.db.models import Q
from django.db.models.aggregates import Count
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from app.models import Category, Post


#==========================
# HOME VIEW
#==========================
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(
            status='published'
            ).select_related('category', 'author')

        # FILTRER PAR CATEGORIE
        category_slug = self.kwargs.get('category_slug') or self.request.GET.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset

    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_at')[:4]
        context['categories'] = Category.objects.annotate(
            post_count=Count('posts', filter=Q(posts__status='published'))
        )
        context['current_category'] = self.kwargs.get('category_slug') or self.request.GET.get('category')
        return context 



#==========================
# POST LIST VIEW
#==========================
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(
            status='published'
            ).select_related('category', 'author').order_by('-published_at')
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(posts__status='published').distinct()
        context['current_category'] = self.kwargs.get('category_slug')
        return context

#==========================
# POST DETAIL VIEW
#==========================
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_at')[:3]
        return context
