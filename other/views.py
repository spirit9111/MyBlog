from django.shortcuts import render

# Create your views here.
from django.views import View


def page_not_found(request):
	return render(request, '404.html')


class AboutMeView(View):
	"""AboutMe"""
	# todo
	pass
