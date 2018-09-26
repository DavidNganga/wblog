from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Blog(models.Model):
     title = models.CharField(max_length=20)
     post = models.CharField(max_length=200)
     videofile= models.FileField(upload_to='videos/', null=True)
     image= models.ImageField(upload_to = 'images/',null = True)
     event_date = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])
