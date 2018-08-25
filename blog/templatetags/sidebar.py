import logging
import random

from django import template

from blog.models import Tag, Article,Category
from other.models import MottoList

register = template.Library()


@register.simple_tag
def get_hot_articles():
	"""获取热门文章"""
	try:
		sidebar_articles = Article.objects.order_by('-views').filter(is_show=True, views__gt=0)[:5]  # 侧边栏
	except Exception as e:
		logging.error(e)
		sidebar_articles = []
	return sidebar_articles


@register.simple_tag
def get_tags():
	"""tag云"""
	try:
		tags = Tag.objects.all()
	except Exception as e:
		logging.error(e)
		tags = []
	return tags


@register.simple_tag
def get_category():
	"""categories"""
	try:
		categories = Category.objects.all()
	except Exception as e:
		logging.error(e)
		categories = []
	return categories



@register.filter()
def type_filter(value):
	if value == 'category':
		return '分类'
	elif value == 'tag':
		return '标签'
	else:
		return ''


# todo
@register.simple_tag
def everyday_motto():
	"""每日一句"""
	try:
		mottos = MottoList.objects.all()
		num = random.randint(0, mottos.count())
		result = mottos[num].content
	except Exception as e:
		logging.error(e)
		result = '这不是一个bug,这只是一个未列出来的特性.'

	return result
