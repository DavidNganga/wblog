from django.db import models

# Create your models here.
class Blog(models.Model):
     title = models.CharField(max_length=20)
     post = models.CharField(max_length=200)
     videofile= models.FileField(upload_to='videos/', null=True)
     image= models.ImageField(upload_to = 'images/',null = True)
