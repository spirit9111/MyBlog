import xadmin
from xadmin import views
from . import models


class BaseSetting(object):
	"""xadmin的基本配置"""
	enable_themes = True  # 开启主题切换功能
	use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
	"""xadmin的全局配置"""
	site_title = "SpiritBlog后台"  # 设置站点标题
	site_footer = "Blog后台管理系统"  # 设置站点的页脚
	menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


class CategoryAdmin(object):
	list_display = ['id', 'name']
	list_per_page = 50


xadmin.site.register(models.Category, CategoryAdmin)


class TagAdmin(object):
	list_display = ['id', 'name']
	list_per_page = 50


xadmin.site.register(models.Tag, TagAdmin)


@xadmin.sites.register(models.Article)
class ArticleAdmin(object):
	list_display = ['id', 'title', 'author', 'category', 'views', 'created_time', ]
	list_per_page = 10
	search_fields = ['title', 'category__name', 'tags__name']
	list_filter = ['is_show', 'is_banner']

# list_editable = ['views', 'created_time'] #有bug
