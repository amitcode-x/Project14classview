from django.db import models
from django.urls import reverse


# Create your models here.


class School(models.Model):
    scname = models.CharField(max_length=100)
    scloc = models.CharField(max_length=100)
    scprinciple = models.CharField(max_length=100)
    
    def __str__(self):
        return self.scname
    
    def get_absolute_url(self):
        return reverse("SchoolDetailView", kwargs={"pk": self.pk})
    
class Student(models.Model):
    scname = models.ForeignKey(School,on_delete=models.CASCADE, related_name="students")
    stname = models.CharField(max_length=100)
    stloc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.stname
    
    def get_absolute_url(self):
        return reverse("StudentDetailView", kwargs={"pk": self.pk})
    
