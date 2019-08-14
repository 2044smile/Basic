from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # :8000/list
    path('list/', views.BookListView.as_view(), name='list'), # :8000/list
    path('create/', views.BookCreateView.as_view(), name='create'), # :8000/create
    path('list/delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete'), # :8000/list/delete/1
    path('list/update/<int:pk>/', views.BookUpdateView.as_view(), name='update'),
]