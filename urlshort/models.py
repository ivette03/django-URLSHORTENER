from django.db import models

# Create your models here.
class URL(models.Model):
   long_url = models.CharField(max_length=500)
   short_url = models.CharField(max_length=10)
   alias = models.CharField(max_length=12)

   def __str__(self):  # Agrega un espacio entre "def" y "__str__"
       return self.short_url
