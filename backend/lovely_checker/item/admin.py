from django.contrib import admin

from .models import Item, CategoryItem, ItemThroughIp, Comment, MenuItem

# Register your models here.
admin.site.register(Item)
admin.site.register(CategoryItem)
admin.site.register(ItemThroughIp)
admin.site.register(Comment)
admin.site.register(MenuItem)
