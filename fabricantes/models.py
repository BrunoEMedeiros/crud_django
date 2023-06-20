from django.db import models
from estados.models import Estado

# Create your models here.
class Fabricante(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    cnpj = models.CharField(max_length=14)
    joined_date = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.razao_social} {self.phone} {self.cnpj} {self.joined_date}"


