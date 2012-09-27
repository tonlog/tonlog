# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from models import Blog
from forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import datetime
import models,toolkit,Arg

#for tonlog blog application:
def index(requeset):
    #获得外链的数据
    outer_links = toolkit.get_outer_links()
    #获得最新博客文章的数据
    blogs = toolkit.get_blogs_content()
    trial = toolkit.get_day_limit(7)

    return render_to_response('index.html', {
        'links': outer_links,
        'blogs': blogs,
        'previous_page': '#' ,
        'next_page':'page/1',
    })

#页面跳转的逻辑判断
def turn_to_page(request, offset=[]):
    total = Blog.objects.count()
    index = int(offset[0]);
    if (index-1) in range(0,total/Arg.num_of_tonlogs_per_page + 1):
        #进行分页获得博客文章
        blogs = toolkit.read_blog_content(index)
        #获得最近8篇的文章数据
        recent = toolkit.get_recent_tonlog()

        previous_page = '/%s' % str(index-1)
        next_page     = '/page/%s' % str(index+1)

        if index-1 <= 0: previous_page = '#';
        if index-1 >= total/Arg.num_of_tonlogs_per_page: next_page = '#';

        return render_to_response('page.html', {
            'blogs':blogs,
            'previous_page':previous_page,
            'next_page':next_page,
            'recents': recent,
            })
    else:
        return render_to_response('NonExists.html', {})
























def searchBlog(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(tag_icontains=query)
        )
        results = Blog.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response('searchBlog.html', {'results':results , 'query':query})

DEFAULT_MAIL_RECEIVER = 'tonie.tonieh.h@gmail.com'
DEFAULT_MAIL_SENDER = 'your_mail_name@example.com'

@csrf_protect
def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            send_mail('feedback for you: %s' % (topic,),
                message,
                sender,
                [DEFAULT_MAIL_RECEIVER],
            )
            return HttpResponseRedirect("/contactUs/thx")
    else:
        form = ContactForm()
    return render_to_response("contactUs.html",{'form':form},context_instance=RequestContext(request))

def thankU(request):
    return render_to_response("", {})
