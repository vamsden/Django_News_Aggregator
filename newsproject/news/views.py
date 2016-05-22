from django.shortcuts import render
from .models import Article, Feed

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
    context = {

    }
    return render(request, 'news/new_feed.html', context)
