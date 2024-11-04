from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=20, name='username')
    balance = models.DecimalField(max_digits=20, decimal_places=2,  default=0.00)
    age = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.username
class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='owner')
    objects = models.Manager()
