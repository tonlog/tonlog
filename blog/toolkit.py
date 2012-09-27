# -*- coding: utf-8 -*-

import models, MapObject, Arg
import datetime

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
        blogs = models.Blog.objects.all().order_by("-pub_time")[:Arg.num_of_recent_diaplay]
    titleset = blogs.values('title')
    pubtimeset  = blogs.values('pub_time')
    contentset  = blogs.values('content')
    result = []
    for i in range(0, blogs.count()):
        result.append(MapObject.Blog_content(
            titleset[i]['title'],
            pubtimeset[i]['pub_time'],
            contentset[i]['content'],
        ))
    return result

#分页抓取博客内容
def read_blog_content(index):
    blogs = models.Blog.objects.all()
    result = []
    if index * Arg.num_of_tonlogs_per_page <= blogs.count():
        start = (index-1) * Arg.num_of_tonlogs_per_page
        content = blogs[start:start+ Arg.num_of_tonlogs_per_page]
    else:
        start = (index-1) * Arg.num_of_tonlogs_per_page
        content = blogs[start:start+blogs.count()]

    result = get_blogs_content(content)
    return result

#获取最近一段时间的tonlog数
def get_recent_tonlog():
    blogs = models.Blog.objects.all().order_by('-pub_time')[:Arg.num_of_recent_tonlog]
    result = get_blogs_content(blogs)
    return result

#获取最近七天的数据
def get_day_limit(limit_num):
    blogs = models.Blog.objects.all()
    result = blogs.dates("pub_time", "day", order="DESC")
    now = datetime.datetime.today()
    date = result[0]
    date = date - now



    return result