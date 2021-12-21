from django.db import models


class Food(models.Model):
    
    name = models.CharField()
    #img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    dis = models.TextField()

