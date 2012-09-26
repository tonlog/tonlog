from django.contrib import admin
import models

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'pub_time',)
    ordering = ('pub_time', 'title')
    list_filter = ('pub_time', 'tag')
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog','topic','up_time')
    ordering = ('up_time', 'blog')
    list_filter = ('blog', 'topic')
    search_fields = ('blog','topic')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_line',)
    ordering = ('-tag_line',)

class OuterLinkAdmin(admin.ModelAdmin):
    list_display = ('blog_name','blog_site')

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.OuterLink, OuterLinkAdmin)