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

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'product', 'approved', 'created_date')
    list_filter = ('name', 'approved' )
    # ordering = ['-created_at']
    search_fields = ['name', 'product']

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductImage)
admin.site.register(Contact)
admin.site.register(NewsLetter)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)