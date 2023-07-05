from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from .models import Book

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    login_url = 'account_login'
    
    
    
class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.Special_status'
    

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
    
    
class SearchListView(ListView):
    model = Book
    template_name = 'books/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        return Book.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query)) 


