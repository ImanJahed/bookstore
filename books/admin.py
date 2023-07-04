from django.contrib import admin

from .models import Book, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    # extra = 0

class BookAdmin(admin.ModelAdmin):
    inlines = CommentInline,
    list_display = ['title', 'author', 'price']
    search_fields = ['title', 'author']
    list_filter = ['title', 'created_date']

admin.site.register(Book, BookAdmin)