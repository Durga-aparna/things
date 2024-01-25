from django.db import models

# Create your models here.
class bus(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    FROM=models.CharField(max_length=50,default="devi")
    TO=models.CharField(max_length=50,default="appu")
def __str__(self):
    return self.name
