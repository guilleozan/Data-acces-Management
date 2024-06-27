from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group 
from .forms import ArticleForm
from .models import Article, Category

def home(request):
    return render(request, 'home.html')

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    allowed_roles = ['Administrator', 'Tutor']
    if request.user.groups.filter(name__in=allowed_roles).exists():
        if request.method == 'POST':
            article.delete()
            return redirect('browse_articles')
        return render(request, 'auth/article_confirm_delete.html', {'article': article})
    else:
        return redirect('browse_articles')

def browse_articles(request):
    keyword = request.GET.get('keyword', '')
    category_name = request.GET.get('category', '')

    articles = Article.objects.all().select_related('category')

    if keyword:
        articles = articles.filter(title__icontains=keyword)

    if category_name:
        articles = articles.filter(category__name=category_name)

    categories = Category.objects.all()
    allowed_roles = ['Administrator', 'Tutor']

    return render(request, 'browse_articles.html', {'articles': articles, 'categories': categories, 'allowed_roles': allowed_roles})

@login_required
def create_article(request):
    allowed_roles = ['Administrator', 'Tutor']
    if request.user.groups.filter(name__in=allowed_roles).exists():
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('browse_articles')
        else:
            form = ArticleForm()
        return render(request, 'auth/article_form.html', {'form': form})
    else:
        return redirect('browse_articles')

@login_required
@permission_required('subjects.change_article', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('browse_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'auth/article_form.html', {'form': form})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'auth/article_detail.html', {'article': article})

def signup(request):
    if request.method == 'POST':
        role = request.POST['role']
        request.POST._mutable = True
        del request.POST['role']

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user_role_group = Group.objects.get(name=role)
            user.groups.add(user_role_group)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'auth/logged_out.html')

