import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now, get_default_timezone

class Repository(models.Model):
    name = models.CharField(max_length = 256)
    protocol = models.CharField(max_length = 24)
    host = models.CharField(max_length = 256)
    port = models.IntegerField()
    basepath = models.CharField(max_length = 256)
    
    def __unicode__(self):
        return self.name
    def get_url(self):
        return "%s://%s:%d/%s" % (self.protocol, self.host, self.port, self.basepath)

class Book(models.Model):
    user = models.ForeignKey(User)
    repository = models.ForeignKey(Repository)
    path = models.CharField(max_length = 512)
    title = models.CharField(max_length = 256)
    author = models.CharField(max_length = 256)
    hits = models.IntegerField(default = 0)
    upload_date = models.DateTimeField(auto_now_add = True, default = now())

    
    def __unicode__(self):
        return "%s by %s" % (self.title, self.author)
    def get_url(self):
        return self.repository.get_url() + self.path

class APIKey(models.Model):
    name = models.CharField(max_length = 256)
    key = models.CharField(max_length = 56)
    permissions = models.IntegerField(default = 0)

    def get_permissions(self):
        if self.permissions == 0:
            return 'None'
        elif self.permissions == 1:
            return 'Read'
        elif self.permissions == 2:
            return 'Read/Write'
        else:
            return 'Unknown'
    def __unicode__(self):
        return "%s (%s)" % (self.name, self.get_permissions())
