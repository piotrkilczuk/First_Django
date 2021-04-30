from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post, Author
from posts.views import *


class PostViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response_list = reverse('posts:posts_list')
        self.response_details = reverse("posts:post_details", args=[1])
        self.response_fail_details = reverse("posts:post_details", args=[999])
        self.example_author = Author.objects.create(nick="Ja", email="ja@gmail.com")

    def test_posts_list_GET(self):
        response = self.client.get(self.response_list)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts_list.html")

    def test_posts_list_POST(self):
        data = {"title": "tak", "content": "zawartość", "author": self.example_author}
        response = self.client.post(self.response_list, data=data)
        self.assertEqual(response.status_code, 302)

    def test_post_details(self):
        response = self.client.get(self.response_details)
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(response.status_code, 404)

        p1 = Post.objects.create(title="nie", content="teznie", author=self.example_author)
        self.assertEqual(p1.title, "nie")
        self.assertEqual(p1.id, 1)

        response = self.client.get(self.response_details)
        fail_response = self.client.get(self.response_fail_details)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fail_response.status_code, 404)
        self.assertIn("<a>teznie</a>", response.content.decode())

class AuthorViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response_list = reverse('posts:authors_list')
        self.response_details = reverse("posts:author_details", args=[1])
        self.response_fail_details = reverse("posts:author_details", args=[999])

    def test_authors_list_GET(self):
        response = self.client.get(self.response_list)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/authors_list.html")

    def test_authors_list_POST(self):
        data = {"nick": "Imie", "email": "Imie@gmail.com"}
        response = self.client.post(self.response_list, data=data)
        self.assertEqual(response.status_code, 302)

    def test_author_detail(self):
        response = self.client.get(self.response_details)
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(response.status_code, 404)

        a1 = Author.objects.create(nick="Janek", email="janek@gmail.com")
        self.assertEqual(a1.nick, "Janek")
        self.assertEqual(a1.id, 1)

        response = self.client.get(self.response_details)
        fail_response = self.client.get(self.response_fail_details)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fail_response.status_code, 404)
        self.assertIn("<a>Janek</a>", response.content.decode())