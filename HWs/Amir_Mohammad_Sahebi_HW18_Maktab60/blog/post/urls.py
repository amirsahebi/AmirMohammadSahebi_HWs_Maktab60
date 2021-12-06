from django.urls import path
from django.urls.resolvers import URLPattern

from .views import CommentDetailView, CommentListView, PostDetailView,PostListView,CategoryListView

urlpatterns = [
    path('post/', PostListView, name='post_list'),
    path('post/<int:id>', PostDetailView, name='post_detail'),
    path('category/', CategoryListView, name='category_list'),
    path('comment/', CommentListView, name='comment_list'),
    path('comment/<int:id>', CommentDetailView,name='comment_detail'),
]
