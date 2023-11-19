from django.db import models

# keep a record of the year levels the tutoring business will take on as clients     
class YearLevel(models.Model):
    name = models.CharField(max_length=20)

    # set the label shown on the website to the year level name 
    def __str__(self):
        return self.name
    
# Create your models here.
"""This will be used to assign blogs to subjects"""
class Subject(models.Model):
    subject = models.CharField(max_length=50)
    backgroundColor = models.CharField(max_length=50,blank=True,null=True)
    year_level = models.ManyToManyField(YearLevel, related_name='year_level',blank=True,null=True)
    # the banner image displayed on the subject button
    image = models.ImageField(upload_to='subject_images',blank=True,null=True)
    class Meta:
        ordering = ('subject',)
        verbose_name_plural = 'subjects'
    
    # override the str method so subject is automatically displayed
    def __str__(self):
        return self.subject
    


# DB model for storing the form info for the business owner to review 
class StudentRequest(models.Model):
    subject1 = models.ForeignKey(Subject,name='subject1',related_name='subject1', on_delete=models.CASCADE,blank=True,null=True)
    subject2 = models.ForeignKey(Subject,name='subject2_optional',related_name='subject2', on_delete=models.CASCADE,blank=True,null=True)
    subject3 = models.ForeignKey(Subject,name='subject3_optional',related_name='subject3', on_delete=models.CASCADE,blank=True,null=True)
    subject4 = models.ForeignKey(Subject,name='subject4_optional',related_name='subject4', on_delete=models.CASCADE,blank=True,null=True)
    year_level = models.ForeignKey(YearLevel,name='year_level', on_delete=models.CASCADE)
    student_name = models.CharField(name="student_name",max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # the business can only offer online tutoring to students who are too far away 
    postcode = models.CharField(name="postcode",max_length=255)
    online_only = models.BooleanField(name="online_only")

    are_you_parent_guardian = models.BooleanField(name="are_you_parent_or_guardian")
    parent_guardian_name = models.CharField(name="parent_or_guardian_name",max_length=255)

    # we require at least one piece of contact information, this is enforced in the form cleaning method 
    parent_guardian_email = models.CharField(name="parent_or_guardian_email",max_length=255,blank=True,null=True)
    student_email = models.CharField(name="students_email",max_length=255,blank=True,null=True)
    phone_number = models.CharField(name="phone_number",max_length = 10,blank=True,null=True)

