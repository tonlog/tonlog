from django.db import models

#class App(models.Model):
#   pass
class Tag(models.Model):
    tag_line = models.CharField(max_length=20)

    def __unicode__(self):
        return self.tag_line

class Blog(models.Model):
    title    = models.CharField(max_length=100, help_text='input your title..')
    pub_time = models.DateTimeField()
    content  = models.TextField()
    tag      = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    topic    = models.CharField(max_length=100, help_text='what is your topic..')
    up_time  = models.DateTimeField()
    words    = models.TextField()
    blog     = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.topic
