from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    departmentName = models.CharField(max_length=64)

    def __str__(self):
        return self.departmentName
    
class Position(models.Model):
    positions = models.CharField(max_length=64)

    def __str__(self):
        return self.positions

class Employee(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    joiningDate = models.DateField()
    ctc = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.firstName} {self.lastName}')