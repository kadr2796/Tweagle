from django.urls import path
from .views import HomeView, ReportPageView, ReportSuccessView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    #path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('report/', ReportPageView.as_view(), name="report_page"),
    path('report_success/', ReportSuccessView.as_view(), name="report_success")
]
