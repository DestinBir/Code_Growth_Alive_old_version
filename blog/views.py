from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def articles(request):
    articles = Article.objects.all()
    
    return render(request, "blog/articles.html", {'arts':articles})

def article(request, id):
    art = Article.objects.get(id=id)

    return render(request, 'blog/article.html', {'art':art})

def search(request):
    query = request.GET.get('query', '')
    
    articles = Article.objects.filter(Q(titre__icontains = query) | Q(body__icontains = query))

    return render(request, 'blog/search.html', {'articles':articles, 'query':query})

def liker(request, id):
    Article = get_object_or_404(Article, id=id)
    Article.likes+=1
    Article.save()
    return redirect('Article_detail', id=id)

@login_required
def delete(request, id, user):
    Article = Article.objects.get(id=id)
    Article.delete()
    return render(request, 'core/user.html', {'Article':Article})
'''
@login_required
def creer(request):
    submitted = False
    
    if request.method == "Article":
        form = MDEditorModleForm(request.Article)
        if form.is_valid():
            Article = form.save(commit=False)
            Article.save()
            url = f'/create/{id}?submitted=True'
            return HttpResponseRedirect(url)
    else:
        form = MDEditorModleForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'core/createArticle.html', {'form':form, 'submitted':submitted})'''

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ArticleForm()
    return render(request, 'blog/create.html', {'form': form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit.html', {'form': form})
