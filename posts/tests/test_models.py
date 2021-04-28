from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Test1", content="To jest test 1", author=Author.objects.create(nick="testowy", email="test@test.pl"))
        Post.objects.create(title="Test2", content="To jest test 2", author=Author.objects.create(nick="testowy2", email="test2@test.pl"))

    def test_post_str(self):
        p1 = Post.objects.get(title="Test1")
        p2 = Post.objects.get(title="Test2")

        self.assertEqual(str(p1), " T: Test1, C: To jest test 1 A: testowy")
        self.assertEqual(str(p2), " T: Test2, C: To jest test 2 A: testowy2")

class AuthorModelTest(TestCase):
    def setUp(self):
        Author.objects.create(nick="test1", email="test1@test.pl")
        Author.objects.create(nick="test2", email="test2@test.pl")

    def test_author_str(self):
        a1 = Author.objects.get(nick="test1")
        a2 = Author.objects.get(nick="test2")

        self.assertEqual(str(a1), "N: test1, E: test1@test.pl")
        self.assertEqual(str(a2), "N: test2, E: test2@test.pl")