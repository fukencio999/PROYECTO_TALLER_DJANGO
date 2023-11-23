from django.db import models

# Create your models here.
from datetime import date
class Project(models.Model):
    title=models.CharField(max_length=100)
    descrption =models.CharField(max_length=250)
    img = models.ImageField(upload_to="portfolio/img")
    url = models.URLField(blank=True)
    date = models.DateField(default= date.today)
    def __Str__(self):
        return self.title
