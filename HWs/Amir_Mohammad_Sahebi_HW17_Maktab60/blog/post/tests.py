from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Post,Comment,Category
from model_mommy import mommy

p1 = Post.objects.get(id=1)
ca1 = Category.objects.filter(id=1)




class TestPost(APITestCase):

    def setUp(self):
        mommy.make(Post,category=ca1, _quantity=10)
        mommy.make(Comment, post=p1 ,_quantity=20)

    def test_post_list(self):
        resp = self.client.get(reverse('post_list'))

        self.assertEqual(len(resp.data),10)
        self.assertEqual(resp.status_code,200)

    def test_comment_list(self):
        resp = self.client.get(reverse('comment_list'))

        self.assertEqual(len(resp.data),20)
        self.assertEqual(resp.status_code,200)
