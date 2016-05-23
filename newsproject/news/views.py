from django.shortcuts import render, redirect
from .models import Article, Feed
from .forms import FeedForm

import datetime
import feedparser
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


# New feed entry form
def feed_new(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            # Feed Parser function
            feedData = feedparser.parse(feed.url)

            # Gets feed title
            feed.title = feedData.feed.title
            feed.save()

            for entry in feedData.entries:
                article = Article()
                article.title = entry.title
                article.url = entry.link
                article.description = entry.description

                # Date formatting
                d = datetime.datetime(*(entry.published_parsed[0:6]))
                dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                article.publication_date = dateString
                article.feed = feed
                article.save()

            # redirects to feed_list using redirect
            return redirect('news.views.feeds_list')
    else:
        form = FeedForm()
    context = {
        'form': form
    }
    return render(request, 'news/new_feed.html', context)
