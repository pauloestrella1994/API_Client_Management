from django.db import models


class Departament(models.Model):
    departament_name = models.CharField(max_length=100, help_text="departament's name")

    def __str__(self):
        return self.departament_name
    
