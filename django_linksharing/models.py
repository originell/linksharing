from django.db import models
from django.contrib.auth.models import User
import datetime

class Link(models.Model):
    '''
    A Link created by some (l)user.
    '''

    created = models.DateTimeField(editable=False, default=datetime.datetime.now)
    author = models.ForeignKey(User, editable=False)

    url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.url.replace('http://', '').replace('www.', '')
