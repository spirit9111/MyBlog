from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class CommentView(View):
	"""评论"""

	def post(self, request):
		if not request.session.get('is_login', None):
			return redirect("/login")
		comment = request.POST.get('comment', None)
		article_id = request.POST.get('article_id', None)
		# parent = request.POST.get('parent', None)  # 可以为空
		# user = request.POST.get('user', None)

		if not all([comment, article_id]):
			message = '参数不足'
			return redirect('')

		# if parent:
		# 	# 给评论评论
		# 	pass
		# else:
		# 	# 给文章评论
		# 	pass

		print(comment, article_id)
		return redirect('/')
