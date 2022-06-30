from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StockList(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stocklist")

    def __str__(self):
        return self.name