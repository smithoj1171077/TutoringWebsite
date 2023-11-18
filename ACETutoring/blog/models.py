from django.db import models
from studentrequest.models import Subject
# Create your models here.

"""This represents the attributes of the blogs stored in the database, 
the body paragraph is the only attibute not shown on the index tabs on the front page, the user has to click on it to see it"""

class Blog(models.Model):
    subject = models.ForeignKey(Subject,related_name='blogs',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images',blank=True,null=True)
    body_paragraph = models.CharField(max_length = 3000)