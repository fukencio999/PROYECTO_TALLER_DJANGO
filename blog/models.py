from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="blog/img")
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.title
