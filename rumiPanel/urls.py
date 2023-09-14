from django.urls import path
from .views import (
    HomepageTemplateView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('Books/', BookListView.as_view(), name='book_list'),
    path('Book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('BookCreate/', BookCreateView.as_view(), name='book_create' ),
    path('Book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('Book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
