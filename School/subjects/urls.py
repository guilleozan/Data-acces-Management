from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse_articles, name='browse_articles'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.create_article, name='create_article'),
    path('article/edit/<int:pk>/', views.edit_article, name='edit_article'),
    path('article/delete/<int:pk>/', views.delete_article, name='delete_article'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
