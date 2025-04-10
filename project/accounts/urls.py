from django.urls import path
from django.contrib.auth import views as auth_views
from . import apis

urlpatterns = [
    path('', apis.home, name='home'),
    path('register/', apis.register, name='register'),
    path('login/', apis.login_view, name='login'),
    path('logout/', apis.logout_view, name='logout'),
]