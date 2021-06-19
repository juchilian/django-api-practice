from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.PositiveBigIntegerField(blank=False, null=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)