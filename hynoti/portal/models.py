# from django.db import models
from djongo import models

        
class PortalNotice(models.Model):
    _id = models.ObjectIdField()
    category = models.CharField(max_length=4)
    title = models.CharField(max_length=64)
    writer = models.CharField(max_length=32)
    date = models.DateTimeField()
    content = models.TextField()
    file = models.TextField()
    
    class Meta:
        db_table = 'portal_notice'