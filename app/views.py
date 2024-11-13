from django.shortcuts import render
from rest_framework import generics
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title','author']
    filterset_fields = ['category', 'date', 'views']

class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.PostListSerializer
    queryset = models.Post.objects.all()

def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PostListSerializer
        return serializers.PostUpdateSerializer
