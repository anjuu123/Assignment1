from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    dateofbirth = models.DateField()
    rollno = models.IntegerField()
    deptname = models.CharField(max_length=100)
    coursename = models.CharField(max_length=100)
    semester = models.IntegerField()



class Department(models.Model):
    deptname=models.CharField(max_length=255)
    numofcourse=models.IntegerField()
    numofteacher=models.IntegerField()