from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .serializers import CategorySerializer, CommentDetailSerializer, Commentserializer,PostSerializer,PostDetailSerializer




from .models import Category, Comment, Post

@api_view(['GET'])
def PostListView(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(data=serializer.data,status=200)
   
@api_view(['GET'])
def PostDetailView(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostDetailSerializer(post)

    return Response(data=serializer.data, status=200)

@api_view(['GET'])
def CategoryListView(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(data=serializer.data, status=200)

@api_view(['GET'])
def CommentListView(request):
    comments = Comment.objects.all()
    serializer = Commentserializer(comments, many=True)

    return Response(data=serializer.data, status=200)

@api_view(['GET'])
def CommentDetailView(request, id):
    comment = get_object_or_404(Comment, id=id)
    serializer = CommentDetailSerializer(comment)

    return Response(data=serializer.data, status=200)

@api_view(['GET'])
def CategoryDetailView(request,id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)

    return Response(data=serializer.data, status=200)