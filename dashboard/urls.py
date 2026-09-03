from django.urls import path

from dashboard.views import AddCategoryView, AddPostView, CategoryDeleteView, CategoryUpdateView, DashboardView, ListCategoriesView, PostsListView, PostUpdateView, PostDeleteView  



urlpatterns = [
    path('home/', DashboardView.as_view(), name='dashboard-home'),
    path('posts-list/', PostsListView.as_view(), name='posts-list'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('categories/', ListCategoriesView.as_view(), name='categories-list'),
    path('category/<str:slug>/update/', CategoryUpdateView.as_view(), name='update-category'),
    path('category/<str:slug>/delete/', CategoryDeleteView.as_view(), name='delete-category'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='update-post'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='delete-post'),
]
