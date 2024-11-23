from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length= 100)
    type = models.CharField(max_length= 100)
    dist = models.IntegerField(default = 0)
    desc = models.CharField(max_length= 1000)

    def __str__(self) -> str:
        return self.name