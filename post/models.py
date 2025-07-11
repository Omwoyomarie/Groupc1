from django.db import models

# Create your models here.
from django.db import models

class ItemList(models.Model):
    sample_item = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.sample_item
