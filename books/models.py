from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    summary = models.CharField(max_length=255, null=True)
    price = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f"{self.name}"