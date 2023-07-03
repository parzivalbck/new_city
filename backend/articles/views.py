from django.shortcuts import render
from .models import Article, New, NewCategorie, Historie
from .serializers import ArticleSerializer, NewSerializer, NewCategorieSerializer, HistorieSerializer
from rest_framework import generics

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class NewCategorieListCreate(generics.ListCreateAPIView):
    queryset = NewCategorie.objects.all()
    serializer_class = NewCategorieSerializer
    
class NewListCreate(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer

class HistorieListCreate(generics.ListCreateAPIView):
    queryset = Historie.objects.all()
    serializer_class = HistorieSerializer