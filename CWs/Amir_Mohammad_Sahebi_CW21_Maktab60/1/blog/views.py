from django.http.response import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from blog.models import Post

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import generics, mixins

from blog.serializers import *


# @api_view(['GET', 'POST'])
# def post_list_create(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(published=True).all()
#         serializer = PostSerializer(posts, many=True)
#
#         return Response(data=serializer.data, status=200)
#
#     elif request.method == 'POST':
#         serializer = PostCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         post = serializer.save()
#
#         post.creator = request.user
#         post.save()
#
#         resp_serializer = PostSerializer(post)
#         return Response(data=resp_serializer.data, status=201)


# class PostList(APIView):
#
#     def get(self, request):
#         posts = Post.objects.filter(published=True).all()
#         serializer = PostSerializer(posts, many=True)
#
#         return Response(data=serializer.data, status=200)
#
#     def post(self, request):
#         serializer = PostCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         post = serializer.save()
#
#         post.creator = request.user
#         post.save()
#
#         resp_serializer = PostSerializer(post)
#         return Response(data=resp_serializer.data, status=201)


class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.filter(published=True).all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

    def create(self, request, *args, **kwargs):
        # PostCreateSerializer(data=request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = self.perform_create(serializer)
        resp_serializer = PostSerializer(post)
        headers = self.get_success_headers(serializer.data)
        return Response(resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail_update_delete(request, id):
#     # try:
#     #     post = Post.objects.get(id=id)
#     # except Post.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)

#     post = get_object_or_404(Post, id=id)

#     if request.method == "GET":
#         serializer = PostDetailSerializer(post)
#         return Response(data=serializer.data, status=200)

#     elif request.method == 'PUT':
#         if post.creator != request.user:
#             return Response(data={'msg': 'this post owned by another user'}, status=400)

#         serializer = PostUpdateSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         updated_post = serializer.save()
#         resp_serializer = PostDetailSerializer(updated_post)
#         return Response(resp_serializer.data, status=200)

#     elif request.method == 'DELETE':
#         if post.creator != request.user:
#             return Response(data={'msg': 'this post owned by another user'}, status=400)
#         post.delete()

#         return Response(status=204)
