from django.test import TestCase
from .models import Category, Article, Keyword, ArticleKeyword

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

class ArticleModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Test Category")
        Article.objects.create(title="Test Article", category=category)

    def test_article_title(self):
        article = Article.objects.get(title="Test Article")
        self.assertEqual(article.title, "Test Article")

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