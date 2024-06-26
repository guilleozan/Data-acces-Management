from django.contrib import admin
from django.urls import path, include
from subjects import views as subject_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('subjects.urls')),
    path('', subject_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('browse_articles/', subject_views.browse_articles, name='browse_articles'),
    path('add_article/', subject_views.add_article, name='add_article'),
    path('article/<int:article_id>/', subject_views.article_detail, name='article_detail'),
    path('signup/', subject_views.signup, name='signup'),
    path('login/', subject_views.login_view, name='login'),
    path('logout/', subject_views.logout_view, name='logout'),
]