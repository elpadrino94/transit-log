from django.urls import path

from dashboard.views import AddCategoryView, AddPostView, DashboardView



urlpatterns = [
    path('home/', DashboardView.as_view(), name='dashboard-home'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
]
