from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from app.models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            status='published'
            ).select_related('category', 'author')

    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_at')[:4]
        return context



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            status='published'
            ).select_related('category', 'author').order_by('-published_at')

#==========================
# POST DETAIL
#==========================
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_at')[:3]
        return context
