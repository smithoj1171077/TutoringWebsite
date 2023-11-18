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
    
# keep a record of the year levels the tutoring business will take on as clients     
class YearLevel(models.Model):
    name = models.CharField(max_length=20)

# DB model for storing the form info for the business owner to review 
class StudentRequest(models.Model):
    subject1 = models.ForeignKey(Subject,name='subject 1',related_name='subject1', on_delete=models.CASCADE,blank=True,null=True)
    subject2 = models.ForeignKey(Subject,name='subject 2 (optional)',related_name='subject2', on_delete=models.CASCADE,blank=True,null=True)
    subject3 = models.ForeignKey(Subject,name='subject 3 (optional)',related_name='subject3', on_delete=models.CASCADE,blank=True,null=True)
    subject4 = models.ForeignKey(Subject,name='subject 4 (optional)',related_name='subject4', on_delete=models.CASCADE,blank=True,null=True)
    year_level = models.ForeignKey(YearLevel,name='year level', on_delete=models.CASCADE)
    student_name = models.CharField(name="student name",max_length=255)
    parent_guardian_name = models.CharField(name="parent/guardian email",max_length=255)
    parent_guardian_email = models.CharField(name="parent/guardian name",max_length=255)
    student_email = models.CharField(name="students email",max_length=255)
    postcode = models.CharField(name="postcode",max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    online_only = models.BooleanField(name="online only")
    are_you_parent_guardian = models.BooleanField(name="are you parent/guardian")
    phone_number = models.CharField(name="phone number",max_length = 10)

