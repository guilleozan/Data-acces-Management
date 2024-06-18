from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Article, Category
from .forms import ArticleForm

# Otras vistas...

def home(request):
    return render(request, 'subjects/home.html')

def is_tutor(user):
    return user.groups.filter(name='Tutors').exists()

def is_admin(user):
    return user.is_superuser

def browse_articles(request):
    category = request.GET.get('category')
    keyword = request.GET.get('keyword')
    articles = Article.objects.all()

    if category:
        articles = articles.filter(category__name=category)
    if keyword:
        articles = articles.filter(title__icontains=keyword)
    
    categories = Category.objects.all()

    return render(request, 'subjects/browse_articles.html', {'articles': articles, 'categories': categories})

@login_required
@user_passes_test(is_tutor)
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('browse_articles')
    else:
        form = ArticleForm()
    return render(request, 'subjects/article_form.html', {'form': form})

@login_required
@user_passes_test(is_tutor)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('browse_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'subjects/article_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('browse_articles')
    return render(request, 'subjects/article_confirm_delete.html', {'article': article})
