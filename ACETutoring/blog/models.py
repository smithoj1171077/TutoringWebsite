from django.db import models

# Create your models here.

"""This will be used to assign blogs to subjects"""
class Subject(models.Model):
    subject = models.CharField(max_length=50)
    backgroundColor = models.CharField(max_length=50,blank=True,null=True)
    # the banner image displayed on the subject button
    image = models.ImageField(upload_to='subject_images',blank=True,null=True)
    class Meta:
        ordering = ('subject',)
        verbose_name_plural = 'subjects'
    
    # override the str method so subject is automatically displayed
    def __str__(self):
        return self.subject


"""This represents the attributes of the blogs stored in the database, 
the body paragraph is the only attibute not shown on the index tabs on the front page, the user has to click on it to see it"""

class Blog(models.Model):
    subject = models.ForeignKey(Subject,related_name='blogs',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images',blank=True,null=True)
    body_paragraph = models.CharField(max_length = 3000)