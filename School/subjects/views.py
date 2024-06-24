from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ArticleForm
from .models import Article, Category  # Asegúrate de importar Category si no lo has hecho ya

def home(request):
    return render(request, 'home.html')

def browse_articles(request):
    keyword = request.GET.get('keyword', '')
    category_name = request.GET.get('category', '')

    articles = Article.objects.all()

    if keyword:
        articles = articles.filter(title__icontains=keyword)

    if category_name:
        articles = articles.filter(category__name=category_name)

    categories = Category.objects.all()

    return render(request, 'browse_articles.html', {'articles': articles, 'categories': categories})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_articles')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'logged_out.html')


