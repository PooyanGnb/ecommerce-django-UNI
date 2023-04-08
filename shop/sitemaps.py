from django.contrib.sitemaps import Sitemap
from shop.models import Product
from django.urls import reverse

class ShopSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_at
    
    def location(self, item):
        return reverse('shop:detail', kwargs={'slug':item.slug})

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['shop:index', 'shop:cart', 'shop:contact', 'shop:checkout']

    def location(self, item):
        return reverse(item)