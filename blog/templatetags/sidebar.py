from django import template

from blog.models import Tag, Article

register = template.Library()


@register.simple_tag
def get_hot_articles():
	"""获取热门文章"""
	sidebar_articles = Article.objects.order_by('-views')[:5]  # 侧边栏
	return sidebar_articles


@register.simple_tag
def get_tags():
	"""tag云"""
	tags = Tag.objects.all()
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
