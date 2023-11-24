from django.db import models
from studentrequest.models import Subject
from django.contrib.auth.models import User

# Create your models here.

# this class has the fields of the books sold on the site
class RevisionBook(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to='store_images')
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
    

    
# a data model for the current cart of the user 
class CartItem(models.Model):
    product = models.ForeignKey(RevisionBook,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
