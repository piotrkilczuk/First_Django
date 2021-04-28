from django.test import TestCase, Client
from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


class PostFormTest(TestCase):
    def setUp(self):
        Author.objects.create(nick="adam", email="adam@adam.pl")

    def test_post_save_correct_data(self):
        data = {"title": "aaa", "content": "aaaa", "author": Author.objects.get(nick="adam")}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Post)
        self.assertEqual(r.title, "aaa")
        self.assertEqual(r.id, 1)
        self.assertEqual(r.author, Author.objects.get(nick="adam"))