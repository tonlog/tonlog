# -*- coding: utf-8 -*-

import urllib
st = "tonie黄曦"

t = urllib.quote(st)
#t = urllib.unquote(t)
print t

import blog.models
import datetime


import pytz
blogs = blog.models.Blog.objects.all()
result = blogs.dates("pub_time", "day", order="DESC")
now = datetime.datetime.today().replace(tzinfo=pytz.utc,hour=0, minute=0,second=0)


print now

