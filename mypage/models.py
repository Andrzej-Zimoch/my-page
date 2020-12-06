from django.db import models


# Create your models here.
# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='pics',blank=True, null=True)
    detail_pic = models.ImageField(upload_to='dt_pics',blank=True, null=True)
    git_link = models.CharField(max_length=250,default="")
    web_link = models.CharField(max_length=250,default="",blank=True, null=True)
    body = models.TextField(default="")
    slug = models.SlugField(max_length=250, default='',unique=True)


    objects=models.Manager()
    def __str__(self):
        return self.title

    
   