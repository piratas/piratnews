# -*- encoding: utf-8 -*-
from django.shortcuts import render

from opps.channels.models import Channel
from opps.articles.models import Post

def index(request):
	template_name = 'index.html'
	context = {}
	channels = Channel.objects.all()
	channels = channels.filter(parent=None)
	posts = Post.objects.all().order_by('-date_update')
	posts = posts.filter(show_on_root_channel=True)
	slider = []
	temp_channels = []
	
	for channel in channels:
		post = posts.filter(channel_id = channel.id)

		if post:
			slider.append(post[0])

		if len(post) > 1:
			post = post[0:2]
		elif len(post) == 1:
			post = post[:1]

		temp_channels.append([channel, post])

	count = len(temp_channels)
	i = 0
	container = []
	while count > 0:
		if count  > 1:
			container.append([temp_channels[i], temp_channels[i+1]])
		else:
			container.append([temp_channels[i]])

		count = count - 2
		i = i + 2

	context['channels'] = channels
	context['containers'] = container
	context['slider'] =  slider
	if slider:
		context['slide_active'] = slider[0]

	return render(request, template_name, context)
