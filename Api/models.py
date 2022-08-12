from django.db import models

# Create your models here.

class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    eid = models.IntegerField()

    def __str__(self):
        return self.fname
    