from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StockList(models.Model):
    name = models.CharField(max_length=50, null=False)
    symbol = models.CharField(max_length=10, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stocklist", null=False)

    def __str__(self):
        return self.name