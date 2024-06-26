from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse_articles, name='browse_articles'),
    path('add/', views.add_article, name='add_article'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]