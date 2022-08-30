from django.db import models

# Create your models here.


# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    PATH_CHOICES = [
        ('AWS', 'AWSDevOps'),
        ('FS', 'FullStack'),
        ('DS', 'DataScience'),
    ]


    full_name = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email=models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)
    path=models.CharField(max_length=20, choices=PATH_CHOICES)

    def __str__(self):
        return f"{self.number}-{self.full_name}"