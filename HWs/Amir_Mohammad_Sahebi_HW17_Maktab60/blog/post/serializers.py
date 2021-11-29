from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import Category, Post, Comment



class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'id', 'created_at']

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'name', 'created_at']

class PostDetailSerializer(serializers.ModelSerializer):
    comment = Commentserializer(many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'name', 'caption', 'category', 'comment', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','parent']



