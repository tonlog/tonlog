from django.contrib import admin
import models

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'pub_time',)

class CommentAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Tag, TagAdmin)