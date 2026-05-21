from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='airlines/')

    def __str__(self):
        return self.name