from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),  # :8000/account/signup
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]