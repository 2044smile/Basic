from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BookForm

from .models import Book

def index(request):
    return render(request, 'books/index.html')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title','author','text','publisher','bookimage']
    success_url = reverse_lazy('list')

class BookUpdateView(UpdateView):
    model = Book
    template_name_suffix = '_update_form'
    form_class = BookForm
    success_url = '/list'

    def edit(request,pk):
        bk = Book.objects.get(pk=pk)
        return render(request, 'books/book_update_form.html', bk)


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/list'

