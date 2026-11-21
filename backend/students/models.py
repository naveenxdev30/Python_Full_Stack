from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department =models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    image_url=models.URLField(blank=True)
    stock=models.PositiveIntegerField(default=10)
    def __str__(self):
        return self.name
# #model - Database structure
# #views - Application Logic
# #Template - HTML User Interface
# #URL - connects the browser requests to views
# #these are the orm operations
# #retrieve the student by name:
# #retrieve only the email
# count total students
# update the student's age