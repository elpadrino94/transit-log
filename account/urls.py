
from django.urls import path

from account.views import login_view, register_view
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]