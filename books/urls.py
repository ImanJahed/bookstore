from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('<uuid:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('add', views.BookCreateView.as_view(), name='book-add'),
    path('<uuid:pk>/edit', views.BookUpdateView.as_view(), name='book-edit'),
    path('<uuid:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
]
