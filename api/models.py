from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.name}"