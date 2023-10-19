from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
# Register your models here.

class NewsAdmin(ModelAdmin):
    list_display = ['id', 'photo']

    fieldsets = (
        ('Add News', {'fields':['descripton', 'photo'], 'classes':['wide']}),
    )

    list_per_page = 5


class CategoryAdmin(ModelAdmin):
    list_display = ['id','name']
    fieldsets = (
        ('Add Category', {'fields':['name'], 'classes':'wide'}),
    )

    search_fields = ['name',]

class ArticleAdmin(ModelAdmin):
    list_display = ['name', 'photo', 'category']
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)