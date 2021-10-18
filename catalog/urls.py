from django.urls import path
from . import views
from django.conf.urls import url
from . import models
from django.urls import include
import re

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^post_list/$', views.PostListView.as_view(), name='post_list'),
    url(r'^post_list/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
]

urlpatterns += [
    url(r'^author_list/$', views.AuthorListView.as_view(), name='author_list'),
    url(r'^author_list/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),
]
