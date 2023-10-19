from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

# Create your views here.

class NewsView(generics.GenericAPIView):
    serializer_class = NewsSerializer

    def get(self, request):
        news = News.objects.all()
        serializers = self.get_serializer(news, many=True)
        data = serializers.data

        return Response(data, status=status.HTTP_200_OK)
    
class CategoryView(generics.GenericAPIView):

    serializer_class = CategorySerializer

    def get(self, request):
        categorys = Category.objects.all()
        serializers = self.get_serializer(categorys, many=True)
        data = serializers.data

        return Response(data, status=status.HTTP_200_OK)
    
class ArticalView(generics.GenericAPIView):
    serializer_class = ArticalSerizlizer

    def get(self, request):
        articles = Article.objects.all()
        serializer = self.get_serializer(articles, many=True)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class RelatedArticleView(generics.GenericAPIView):
    serializer_class = ArticalSerizlizer

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        article_related = category.article_cat.all()
        serializer = self.get_serializer(article_related, many=True)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)


class SingleArticleView(generics.GenericAPIView):
    serializer_class = ArticalSerizlizer

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = self.get_serializer(article, many=False)
        data = serializer.data

        return Response(data, status=status.HTTP_200_OK)
    

class SearchView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticalSerizlizer
