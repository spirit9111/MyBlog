from django.contrib import admin
from . import models


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	list_per_page = 50


class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']
	list_per_page = 50


class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'category', 'views', 'created_time', ]
	list_per_page = 50
	list_filter = ['tags', 'category']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Article, ArticleAdmin)
