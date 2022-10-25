from email import message
from email.headerregistry import Address
from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    ephn = models.IntegerField()
    esalary = models.IntegerField()

    def __str__(self):
        return str(self.ename) 


  





