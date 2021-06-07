from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Report

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Report
    template_name = 'home.html'

#class ArticleDetailView(DetailView):
#    model = Post
#   template_name = 'article_detail.html'

class ReportPageView(CreateView):
    model = Report
    template_name = 'report_page.html'
    fields = '__all__'

class ReportSuccessView(TemplateView):
    model = Report
    template_name = 'report_success.html'