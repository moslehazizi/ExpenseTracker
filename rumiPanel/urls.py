from django.urls import path
from . import views
from .views import (
    HomepageTemplateView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    SearchResultsListView,
    SearchBoxTemplateView,
    GetReportTemplateView,
)

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('Books/', BookListView.as_view(), name='book_list'),
    path('Book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('BookCreate/', BookCreateView.as_view(), name='book_create' ),
    path('Book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('Book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('searchforcalculation/', SearchBoxTemplateView.as_view(), name='book_search'),
    path('getReports/', GetReportTemplateView.as_view(), name='get_reports'),
    path('categoryChartReport/', views.category_chart_report, name='chart_category'),
    path('publisherChartReport/', views.publisher_chart_report, name='chart_publisher')
]
