from django.contrib.syndication.views import Feed
from django.urls import reverse
from shop.models import Product

class LatestEntriesFeed(Feed):
    title = "New posts"
    link = "/rss/feed"
    description = "Amazing posts about different thing to read"

    def items(self):
        return Product.objects.filter(status=1)

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description[:50] + '...'