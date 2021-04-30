from django.test import TestCase, Client
from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


class PostFormTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(nick="adam", email="adam@adam.pl")

    def test_post_save_correct_data(self):
        data = {"title": "aaa", "content": "aaaa", "author": self.author}
        self.assertEqual(Post.objects.count(), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Post)
        self.assertEqual(r.title, "aaa")
        self.assertEqual(r.id, 1)
        self.assertEqual(r.author, self.author)

class AuthorFormTest(TestCase):
    
    def test_author_form(self):
        self.assertEqual(Author.objects.count(), 0)
        data = {"nick": "Adam", "email": "Adam@gmail.com"}
        form = AuthorForm(data=data)
        r = form.save()
        self.assertIsInstance(r, Author)
        self.assertEqual(r.nick, "Adam")
        self.assertEqual(r.id, 1)
        
        data = {"nick": "Adam", "email": "Nieadam@gmail.com"}
        form = AuthorForm(data=data)
        with self.assertRaises(ValueError):
            form.save()

        data = {"nick": "Nieadam", "email": "Adam@gmail.com"}
        form = AuthorForm(data=data)
        with self.assertRaises(ValueError):
            form.save()

        data = {"nick": "Adam", "email": "Adam@gmail.com"}
        form = AuthorForm(data=data)
        with self.assertRaises(ValueError):
            form.save()