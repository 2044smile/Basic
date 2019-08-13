from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BookForm
from django.conf import settings

from .models import Book

def index(request):
    return render(request, 'books/index.html')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'b_list'

class BookCreateView(CreateView):
    model = Book
    success_url = reverse_lazy('list')
    template_name = 'books/book_form.html'
    context_object_name = 'b_list'
    form_class = BookForm

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title','author','text','publisher','bookimage']
    # form_class = BookForm fields를 사용하거나 form_class를 사용하거나 둘 중 하나를 사용할 수 있다.
    success_url = '/list'

def b_list_delete(request, pk):
    if request.method == 'POST':
        b_list = Book.objects.get(pk=pk)
        b_list.delete()
        return render(request, 'books/book_list.html',{'b_list':Book.objects.all()})

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')
