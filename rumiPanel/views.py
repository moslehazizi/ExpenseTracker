from typing import Any
from .models import Book
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.shortcuts import render



class HomepageTemplateView(generic.TemplateView):
    template_name = 'home.html'

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'pages/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'pages/book_detail.html'

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'pages/book_create.html'
    fields = '__all__'
    
class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'pages/book_edit.html'
    fields = '__all__'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'pages/book_delete.html'
    success_url = reverse_lazy('book_list')

class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = 'book_items'
    template_name = 'pages/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query) | Q(subtitle__icontains=query)
        )

class SearchBoxTemplateView(generic.TemplateView):
    template_name = 'pages/book_search.html'

class GetReportTemplateView(generic.TemplateView):
    template_name = 'pages/get_reports.html'


class CategoryChartListView(generic.ListView):
    model = Book
    template_name= 'pages/chart_category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryChartListView, self).get_context_data(**kwargs)
        context["dictCategory"] = Book.objects.values('category').annotate(count=Count('category'))
        return context
    
    

""" def category_report_chart(request):
    dictCategory = Book.objects.values('category').annotate(count=Count('category'))
    return render(request, 'pages/chart_category.html', {'dictCategory': dictCategory}) """



class PublicationReportChartTemplateView(generic.TemplateView):
    template_name = 'pages/chart_publication.html'