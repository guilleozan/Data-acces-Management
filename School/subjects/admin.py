from django.contrib import admin
from .models import Category, Keyword, User, Article, ArticleKeyword

admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(ArticleKeyword)