import xadmin
from . import models


class CommentAdmin(object):
	list_display = ['id', 'user', 'content', 'created_time', ]
	list_per_page = 10
	search_fields = ['content', 'user__name']


xadmin.site.register(models.Comment, CommentAdmin)
