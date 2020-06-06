from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_dept = models.CharField(max_length=10)

    def __str__(self):
        return self.employee_name



