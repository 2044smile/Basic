from django.forms import ModelForm
from .models import Book

class BookCreate(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','publisher','bookimage']
