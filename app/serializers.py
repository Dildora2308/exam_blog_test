

from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'date', 'views', 'category','image']


class PostListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ['title', 'content', 'author', 'date', 'views', 'category',]




class PostUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            exclude = ("id","date")
