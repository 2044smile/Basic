from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Book

def index(request):
    return render(request, 'books/index.html')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title','author','publisher','bookimage']
    success_url = reverse_lazy('list')

class BookDeleteView(DeleteView):
    model = Book


