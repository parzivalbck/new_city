from django.urls import path
from . import views

urlpatterns = [
    path('api/article/', views.ArticleListCreate.as_view()),
    path('api/news/', views.NewListCreate.as_view()),
    path('api/history', views.HistorieListCreate.as_view())
]