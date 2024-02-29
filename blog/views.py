from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *


def articles(request):
    articles = Article.objects.all()
    
    return render(request, "blog/articles.html", {'arts':articles})

def article(request, id):
    art = Article.objects.get(id=id)

    return render(request, 'blog/article.html', {'art':art})

def search(request):
    query = request.GET.get('query', '')

    articles = Article.objects.filter(Q(titre__icontains = query) | Q(article__icontains = query) | Q(body__icontains = query))

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

@login_required
def creer(request, id):
    submitted = False
    cat = Category.objects.get(id=1)
    if request.method == "Article":
        form = ArticleForm(request.Article)
        if form.is_valid():
            Article = form.save(commit=False)
            Article.slug=makeSlug(Article.title)
            Article.author = User.objects.get(id=id)
            Article.category = cat
            Article.save()
            url = f'/create/{id}?submitted=True'
            return HttpResponseRedirect(url)
    else:
        form = ArticleForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'core/createArticle.html', {'form':form, 'submitted':submitted})
