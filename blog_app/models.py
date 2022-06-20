from django.db import models


class Blog (models.Model):
    title = models.CharField(max_length=10)
    sub_title = models.CharField(max_length=15)
    body = models.CharField(max_length=300)
    author = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)
    #img = models.BinaryField
