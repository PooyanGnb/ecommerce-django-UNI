from django.contrib import admin
from .models import *

# Register your models here.
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('name', 'price', 'counted_views', 'status')
    list_filter = ('status', )
    # ordering = ['-created_at']
    search_fields = ['name', 'description']

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImage)
admin.site.register(Contact)
admin.site.register(NewsLetter)