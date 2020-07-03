from django.db import models
from django.contrib.auth.models import User
from Company.models import Company
from Departament.models import Departament


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the employee")
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    company = models.OneToOneField(Company, on_delete=models.SET_NULL,blank=True, null=True)
    departament = models.OneToOneField(Departament, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
