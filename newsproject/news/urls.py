from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articles_list, name='articles_list'),
    url(r'^feeds/new', views.feed_new, name='feed_new'),
    url(r'^feeds/', views.feeds_list, name='feeds_list'),
]
