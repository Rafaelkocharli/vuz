from django.db import models

# Create your models here.
class University(models.Model):
    name = models.TextField()
    first = models.CharField(max_length=20)
    second = models.CharField(max_length=20, default=None, null=True)
    army = models.IntegerField(default=None, null=True)
    city = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return self.name[:40]

class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
    name = models.TextField()
    point = models.CharField(max_length=20)
    places = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name