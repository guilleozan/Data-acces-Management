from django.test import TestCase
from .models import Category, Article

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