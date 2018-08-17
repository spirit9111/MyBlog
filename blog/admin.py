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
	search_fields = ['title']

	fieldsets = (
		('基本', {'fields': ['title', 'author', 'category', 'tags', 'body', 'image']}),
		('高级', {
			'fields': ['excerpt', 'created_time', 'views', 'is_show', 'is_banner'],
			'classes': ('collapse',)  # 是否折叠显示
		})
	)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.site_header = 'SpiritBlog后台'
admin.site.site_title = 'Blog后台管理系统'
admin.site.index_title = '学习|记录|总结'