from django.db import models

# Create your models here.
class Disc(models.Model):
  manufacturer = models.CharField(max_length=50)
  plastic = models.CharField(max_length=50)
  mold = models.CharField(max_length=50)
  flight = models.TextField(max_length=250)

  def __str__(self):
    return f'{self.plastic} {self.mold}'


