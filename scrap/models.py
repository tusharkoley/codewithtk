

from django.db import models
import datetime
from django.utils import timezone


class Index(models.Model):
	site_url = models.CharField(max_length=200)
	search_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.site_url



class Results(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    sl_no = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=2000)
    searched_status=models.CharField(max_length=200, default ='')
    searched_by=models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField(default=timezone.now)


def __str__(self):
        return self.title
    

 