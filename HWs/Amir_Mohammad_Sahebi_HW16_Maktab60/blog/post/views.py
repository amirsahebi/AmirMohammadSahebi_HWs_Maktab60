from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Category, Comment, Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def CategoryListView(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html',{'categories':categories})

def CategoryDetailView(request,slug):
    category = Category.objects.filter(slug=slug)[0]
    return render(request,'category_detail.html',{'category':category})