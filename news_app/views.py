from django.shortcuts import render
from rest_framework.response import Response
""" from rest_framework.views import APIView """ # class based views
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# Create your views here.


# Category CRUD

class CategoryView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

# Journalist CRUD

class JournalistView(generics.ListCreateAPIView):
    queryset = JournalistModel.objects.all()
    serializer_class = JournalistSerializer


# Article CRUD

# READ
class ArticleViewAll(generics.ListAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = LimitOffsetPagination  # or PageNumberPagination
    pagination_class.page_size = 1  # Set default page size

# CREATE
class ArticleViewCreate(generics.ListCreateAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewDetail(generics.RetrieveAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'Article_id'
    

# UPDATE
class ArticleViewUpdate(generics.UpdateAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer


# DELETE
class ArticleViewDelete(generics.DestroyAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer


