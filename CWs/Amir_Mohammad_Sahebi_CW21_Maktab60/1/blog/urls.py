

from django.urls import path
from blog.models import Post
from blog.views import *

urlpatterns = [
    path('post/', PostList.as_view(), name='post_list'),
    # path('post/<int:id>/', post_detail_update_delete, name='post_detail'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),


]
