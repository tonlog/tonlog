# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from models import Blog
from forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import models, MapObject

num_of_tonlogs_per_page = 5
num_of_recent_diaplay = 2

#for tonlog blog application:
def index(requeset):
    outer_links = get_outer_links()
    blogs = get_blogs_content()

    return render_to_response('index.html', {
        'links': outer_links,
        'blogs': blogs,
        'previous_page': '#' ,
        'next_page':'page/1',
    })

def turn_to_page(request, offset=[]):
    total = Blog.objects.count()
    index = int(offset[0]);
    if (index-1) in range(0,total/num_of_tonlogs_per_page + 1):
        blogs = read_blog_content(index)

        previous_page = '/%s' % str(index-1)
        next_page     = '/page/%s' % str(index+1)

        if index-1 <= 0: previous_page = '#';
        if index-1 >= total/num_of_tonlogs_per_page: next_page = '#';

        return render_to_response('page.html', {
            'blogs':blogs,
            'previous_page':previous_page,
            'next_page':next_page,
            })
    else:
        return render_to_response('NonExists.html', {})

def page(request):
    return render_to_response('page.html', {})

def displayContent(request, offset):
    if int(offset[0]) >= len(Blog.objects.all()):
        return render_to_response("index.html",{'site': 'baidu.com','namespace':'somthing'})

#抓取外部链接
def get_outer_links():
    outer_linkset = models.OuterLink.objects.all()
    outer_nameset = outer_linkset.values('blog_name')
    outer_siteset = outer_linkset.values('blog_site')
    blogs = []
    for i in range(0, outer_linkset.count()):
        blogs.append(MapObject.Blog_o(outer_nameset[i]['blog_name'],outer_siteset[i]['blog_site']))
    return blogs

#抓取博客内容
def get_blogs_content(blogs = None):
    if blogs is None:
        blogs = models.Blog.objects.all()[:num_of_recent_diaplay]
    titleset = blogs.values('title')
    pubtimeset  = blogs.values('pub_time')
    contentset  = blogs.values('content')
    result = []
    for i in range(0, blogs.count()):
        result.append(MapObject.Blog_content(
            titleset[i]['title'],
            pubtimeset[i]['pub_time'],
            contentset[i]['content'][:100]+"...",
        ))
    return result

#分页抓取博客内容
def read_blog_content(index):
    blogs = models.Blog.objects.all()
    result = []
    if index*num_of_tonlogs_per_page <= blogs.count():
        start = (index-1)*num_of_tonlogs_per_page
        content = blogs[start:start+num_of_tonlogs_per_page]
    else:
        start = (index-1)*num_of_tonlogs_per_page
        content = blogs[start:start+blogs.count()]

    result = get_blogs_content(content)
    return result






















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
