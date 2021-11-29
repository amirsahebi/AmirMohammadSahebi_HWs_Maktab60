from django.urls import path
from django.urls.resolvers import URLPattern

from .views import CategoryDetailView, PostDetailView,PostListView,CategoryListView

urlpatterns = [
    path('<slug:slug>',PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    path('categories/',CategoryListView, name='category_list'),
    path('categories/<slug:slug>',CategoryDetailView, name='category_detail')
]
