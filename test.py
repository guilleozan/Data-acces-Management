# tests.py
from django.test import TestCase
from .models import User, Category, Article, Keyword, ArticleKeyword

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password_hash="testhash", role="Student")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password_hash, "testhash")
        self.assertEqual(user.role, "Student")

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name="Arts")

    def test_category_creation(self):
        category = Category.objects.get(name="Arts")
        self.assertEqual(category.name, "Arts")

class ArticleModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Arts")
        Article.objects.create(category=category, title="Mona Lisa", type="Painting")

    def test_article_creation(self):
        article = Article.objects.get(title="Mona Lisa")
        self.assertEqual(article.title, "Mona Lisa")
        self.assertEqual(article.type, "Painting")
        self.assertEqual(article.category.name, "Arts")

class KeywordModelTest(TestCase):
    def setUp(self):
        Keyword.objects.create(keyword="Impressionism")

    def test_keyword_creation(self):
        keyword = Keyword.objects.get(keyword="Impressionism")
        self.assertEqual(keyword.keyword, "Impressionism")

class ArticleKeywordModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Arts")
        article = Article.objects.create(category=category, title="Mona Lisa", type="Painting")
        keyword = Keyword.objects.create(keyword="Renaissance")
        ArticleKeyword.objects.create(article=article, keyword=keyword)

    def test_article_keyword_creation(self):
        article_keyword = ArticleKeyword.objects.get(article__title="Mona Lisa", keyword__keyword="Renaissance")
        self.assertEqual(article_keyword.article.title, "Mona Lisa")
        self.assertEqual(article_keyword.keyword.keyword, "Renaissance")
