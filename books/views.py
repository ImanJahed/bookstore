from urllib import request
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    
    
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'price', 'content', 'cover', ]
    template_name = 'books/book_update.html'
    
    
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'price', 'content', 'cover', ]
    
    template_name = 'books/book_create.html'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book-list')