# -*- encoding: utf-8 -*-
from django.shortcuts import render

from opps.channels.models import Channel
from opps.articles.models import Post

def index(request):
	template_name = 'index.html'
	context = {}	

	return render(request, template_name, context)
