from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the employee")
    # user = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.name
