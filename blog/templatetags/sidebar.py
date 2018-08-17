from django import template

from blog.models import Tag, Article

register = template.Library()


@register.simple_tag
def get_hot_articles():
	"""获取热门文章"""
	try:
		sidebar_articles = Article.objects.order_by('-views').filter(is_show=True)[:5]  # 侧边栏
	except Exception as e:
		sidebar_articles = []
	return sidebar_articles


@register.simple_tag
def get_tags():
	"""tag云"""
	try:
		tags = Tag.objects.all()
	except Exception as e:
		tags = []
	return tags


@register.filter()
def type_filter(value):
	if value == 'category':
		return '分类'
	elif value == 'tag':
		return '标签'
	else:
		return ''

# todo 每日一句
