from django.db import models


# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    Issue = models.TextField()

    def __str__(self):
        return self.Name
