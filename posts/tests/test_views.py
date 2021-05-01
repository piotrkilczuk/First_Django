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
        self.example_author2 = Author.objects.create(nick="Ja2", email="ja2@gmail.com")

    def test_posts_list_GET(self):
        response = self.client.get(self.response_list)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts_list.html")

        Post.objects.create(title="widok1", content="tekst1", author=self.example_author)
        Post.objects.create(title="widok2", content="tekst2", author=self.example_author2)
        Post.objects.create(title="widok3", content="tekst3", author=self.example_author)
        Post.objects.create(title="widok4", content="tekst4", author=self.example_author2)

        response = self.client.get(self.response_list)

        self.assertIn(" T: widok1, C: tekst1 A: Ja", response.content.decode())
        self.assertIn(" T: widok2, C: tekst2 A: Ja2", response.content.decode())
        self.assertIn(" T: widok3, C: tekst3 A: Ja", response.content.decode())
        self.assertIn(" T: widok4, C: tekst4 A: Ja2", response.content.decode())

    def test_posts_list_POST(self):
        data = {"title": "tak", "content": "zawartość", "author": self.example_author}
        response = self.client.post(self.response_list, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/posts/")

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

        Author.objects.create(nick="Adam1", email="Adam1@gmail.com")
        Author.objects.create(nick="Adam2", email="Adam2@gmail.com")
        Author.objects.create(nick="Adam3", email="Adam3@gmail.com")
        Author.objects.create(nick="Adam4", email="Adam4@gmail.com")

        response = self.client.get(self.response_list)

        self.assertIn("N: Adam1, E: Adam1@gmail.com", response.content.decode())
        self.assertIn("N: Adam2, E: Adam2@gmail.com", response.content.decode())
        self.assertIn("N: Adam3, E: Adam3@gmail.com", response.content.decode())
        self.assertIn("N: Adam4, E: Adam4@gmail.com", response.content.decode())

    def test_authors_list_POST(self):
        data = {"nick": "Imie", "email": "Imie@gmail.com"}
        response = self.client.post(self.response_list, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/posts/authors/")

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