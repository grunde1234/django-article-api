from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination

# Category CRUD
class CategoryView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

# Journalist CRUD
class JournalistView(generics.ListCreateAPIView):
    queryset = JournalistModel.objects.all()
    serializer_class = JournalistSerializer

# Article CRUD
class ArticleViewAll(generics.ListAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = LimitOffsetPagination
    pagination_class.page_size = 1

class ArticleViewCreate(generics.ListCreateAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, FormParser)

class ArticleViewDetail(generics.RetrieveAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'Article_id'

class ArticleViewUpdate(generics.UpdateAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, FormParser)

class ArticleViewDelete(generics.DestroyAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
