from django.shortcuts import render, redirect
from .models import Article, Feed
from .forms import FeedForm

# Create your views here.


def articles_list(request):
    articles = Article.objects.all
    context = {
        'articles': articles
    }
    return render(request, 'news/articles_list.html', context)


def feeds_list(request):
    feeds = Feed.objects.all
    context = {
        'feeds': feeds
    }
    return render(request, 'news/feeds_list.html', context)


def feed_new(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.title = "Title"
            feed.save()
            return redirect('news.views.feeds_list')
    else:
        form = FeedForm()
    context = {
        'form': form
    }
    return render(request, 'news/new_feed.html', context)
