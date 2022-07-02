from django.db import models

# Create your models here.
class AllStocks(models.Model):
    name = models.CharField(max_length=50, null=False)
    symbol = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name