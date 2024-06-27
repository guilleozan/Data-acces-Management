from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('Administrator', 'Administrator'),
        ('Tutor', 'Tutor'),
        ('Student', 'Student'),
    ]
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    class Meta:
        db_table = 'Users'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'Categories'
        
    def __str__(self):
        return self.name
        

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    known_for = models.CharField(max_length=255, blank=True, null=True)
    notable_work = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    medium = models.CharField(max_length=255, blank=True, null=True)
    dimensions = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    designed_by = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        db_table = 'Articles'

class Keyword(models.Model):
    keyword_id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'Keywords'

class ArticleKeyword(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('article', 'keyword')
        db_table = 'ArticleKeywords'

        