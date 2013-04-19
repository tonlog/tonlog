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

#result = blogs.dates("pub_time", "day", order="DESC")
#   date = result[0]

#获取最近数天的数据
def get_day_limit(limit_num=0):
    blogs = models.Blog.objects.all()

    if limit_num<0:
        return blogs

    import pytz
    today = datetime.datetime.today().replace(tzinfo=pytz.utc,hour=0, minute=0,second=0)
    date = today - datetime.timedelta(limit_num)
    result = blogs.filter(pub_time__gte=date)
    return result


