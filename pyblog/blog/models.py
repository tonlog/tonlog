from django.db import models

class Tag(models.Model):
    tag_line = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag_line

class Blog(models.Model):
    title    = models.CharField(max_length=100)
    pub_time = models.DateTimeField()
    content  = models.TextField(blank=True)
    tag      = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    topic    = models.CharField(max_length=100)
    up_time  = models.DateTimeField()
    words    = models.TextField()
    blog     = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.topic

class OuterLink(models.Model):
    blog_name = models.CharField(max_length=30)
    blog_site = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.blog_name