from django.db import models

# Create your models here.
class Estado(models.Model):
    uf = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return f"{self.uf}"


