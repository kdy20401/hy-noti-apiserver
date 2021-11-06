from djongo import models

        
class BsNotice(models.Model):
    _id = models.ObjectIdField()
    category = models.CharField(max_length=4)
    title = models.CharField(max_length=64)
    writer = models.CharField(max_length=32)
    date = models.DateTimeField()
    noticeLink = models.TextField()
    content = models.TextField()
    file = models.TextField()
    
    class Meta:
        db_table = 'bs_notice'