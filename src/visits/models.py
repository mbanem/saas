from django.db import models

# Create your models here.
class PageVisit(models.Model):
  home_page = models.IntegerField(default=0)
  extended  = models.IntegerField(default=0)
  template  = models.IntegerField(default=0)
  python  = models.IntegerField(default=0)
  main = models.IntegerField(default=0)
  login = models.IntegerField(default=0)
