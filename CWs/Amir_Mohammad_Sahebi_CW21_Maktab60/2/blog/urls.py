

from django.urls import path
from blog.views import PostListCreate, PostDetailUpdateDeleteView

urlpatterns = [
    path('post/', PostListCreate.as_view(), name='post_list'),
    path('post/<int:id>/', PostDetailUpdateDeleteView.as_view(), name='post_detail')
]