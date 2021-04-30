from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import posts_list, authors_list

class TestUrls(TestCase):
    def test_resolution_for_posts_list(self):
        resolver = resolve('/posts/')
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_author_lists(self):
        resolver = resolve('/posts/authors/')
        self.assertEqual(resolver.func, authors_list)

    def test_get_object_or_404(self):
        with self.assertRaises(Resolver404):
            resolve('posts/99999999')

    def test_get_object_or_404(self):
        with self.assertRaises(Resolver404):
            resolve('author/99999999')