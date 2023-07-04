from django.contrib import admin

from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    search_fields = ['title', 'author']
    list_filter = ['title', 'created_date']

admin.site.register(Book, BookAdmin)