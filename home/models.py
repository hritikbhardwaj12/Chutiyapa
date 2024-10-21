from django.db import models

# Create your models here.
class Sign_up(models.Model):
    College_Email=models.CharField(max_length=10)
    Gender=models.CharField(max_length=10)
    Branch=models.CharField(max_length=10)
    Year= models.CharField(max_length=10)
    date=models.DateTimeField()
    
    
    def __str__(self):
        return self.College_Email