from django.urls import path

from dashboard.views import AddCategoryView, AddPostView, DashboardView, ListCategoriesView, PostsListView



urlpatterns = [
    path('home/', DashboardView.as_view(), name='dashboard-home'),
    path('posts-list/', PostsListView.as_view(), name='posts-list'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('categories/', ListCategoriesView.as_view(), name='categories-list'),
]
