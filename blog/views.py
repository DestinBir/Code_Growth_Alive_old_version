from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


def articles(request):
    articles = Article.objects.all()
    
    return render(request, "blog/articles.html", {'arts':articles})

def article(request, id):
    art = Article.objects.get(id=id)

    return render(request, 'blog/article.html', {'art':art})

@login_required
def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains = query) | Q(intro__icontains = query) | Q(body__icontains = query))

    return render(request, 'blog/search.html', {'posts':posts, 'query':query})

def liker(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes+=1
    post.save()
    return redirect('post_detail', id=id)

def delete(request, id, user):
    post = Post.objects.get(id=id)
    post.delete()
    return render(request, 'core/user.html', {'post':post})

def creer(request, id):
    submitted = False
    cat = Category.objects.get(id=1)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug=makeSlug(post.title)
            post.author = User.objects.get(id=id)
            post.category = cat
            post.save()
            url = f'/create/{id}?submitted=True'
            return HttpResponseRedirect(url)
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'core/createArticle.html', {'form':form, 'submitted':submitted})
