from __future__ import unicode_literals

from django.db import models

class Complaint(models.Model):
    message = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message
