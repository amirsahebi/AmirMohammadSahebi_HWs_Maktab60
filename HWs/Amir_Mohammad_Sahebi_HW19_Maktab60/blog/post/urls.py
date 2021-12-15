from django.urls import path
from django.urls.resolvers import URLPattern

from .views import CategoryDetailView, CommentDetailView, CommentListView, PostDetailView,PostListView,CategoryListView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_Detail'),
    path('comment/', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetailView.as_view(),name='comment_detail'),
]
