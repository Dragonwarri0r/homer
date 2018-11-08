from django.db import models

#传感器表
class NodePost(models.Model):
    nodeid = models.IntegerField()
    nodename = models.CharField(max_length=8)
    nodestatus = models.BooleanField()
    nodetime = models.DateTimeField()
##    nodedata = models.CharField(max_length=12)


# Create your models here.
