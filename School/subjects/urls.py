from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse_articles, name='browse_articles'),
    path('add/', views.add_article, name='add_article'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]