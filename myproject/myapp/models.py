from django.db import models

class StudentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    roll=models.IntegerField(null=True)
    department=models.CharField(null=True)
    email=models.EmailField(null=True)
    dob=models.DateField(null=True)
    
    def __str__(self):
        return self.name
