# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed

from .models import Post


class AllPostRssFeed(Feed):
    title = "Django"
    link = "/"
    description = "Django 博客教程测试文章"

    def items(self):
        return Post.objects.all()

    def item_tile(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
