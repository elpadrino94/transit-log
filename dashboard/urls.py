from django.urls import path

from dashboard.views import AddCategoryView, AddPostView



urlpatterns = [
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
]
