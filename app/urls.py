from django.urls import path

from app.views import HomeView, PostListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/', PostListView.as_view(), name='post-list'),
]

