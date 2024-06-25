from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ArticleForm
from .models import Article, Category  

"""
I will add a proper add_article, as add article shows articles, 
so problably i'll change that later.

 missing : 
 articles_detailes
 edit_articles
 delete_articles


"""
def home(request):
    return render(request, 'home.html')

def browse_articles(request):
    keyword = request.GET.get('keyword', '')
    category_name = request.GET.get('category', '')

    articles = Article.objects.all().select_related('category')

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


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ArticleForm
from .models import Article, Category

def home(request):
    return render(request, 'home.html')

def browse_articles(request):
    keyword = request.GET.get('keyword', '')
    category_name = request.GET.get('category', '')

    articles = Article.objects.all().select_related('category')

    if keyword:
        articles = articles.filter(title__icontains=keyword)

    if category_name:
        articles = articles.filter(category__name=category_name)

    categories = Category.objects.all()

    return render(request, 'browse_articles.html', {'articles': articles, 'categories': categories})

@login_required
@permission_required('subjects.add_article', raise_exception=True)
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_articles')
    else:
        form = ArticleForm()
    return render(request, 'auth/article_form.html', {'form': form})

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'auth/article_form.html'
    success_url = '/browse_articles/'

    def test_func(self):
        return self.request.user.has_perm('subjects.change_article')

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'auth/article_confirm_delete.html'
    success_url = '/browse_articles/'

    def test_func(self):
        return self.request.user.has_perm('subjects.delete_article')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        
        user = User.objects.create_user(username=username, password=password)
        
        if role == 'Administrator':
            group = Group.objects.get(name='Administrator')
        elif role == 'Tutor':
            group = Group.objects.get(name='Tutor')
        elif role == 'Student':
            group = Group.objects.get(name='Student')
        
        user.groups.add(group)
        login(request, user)
        return redirect('home')
    return render(request, 'auth/signup.html')

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

