from django.db import models
from Company.models import Company
from Departament.models import Departament


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the employee")
    company = models.OneToOneField(Company, on_delete=models.SET_NULL,blank=True, null=True)
    departament = models.OneToOneField(Departament, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
