from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    address       = models.CharField(max_length=255, default=None, verbose_name="Direccion")
    dni           = models.CharField(max_length=255, default=None, verbose_name="DNI")
    telephone     = models.CharField(max_length=255, default=None, verbose_name="Telefono fijo")
    mobile        = models.CharField(max_length=255, default=None, verbose_name="Mobil")
    portrait_img  = models.CharField(max_length=255, default=None, verbose_name="Imagen")
    birth_date    = models.DateField(default=None, verbose_name="Fecha de nacimiento")
    created_at    = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.id

    class Meta:
        db_table: 'candidate'
        verbose_name: 'Candidato'
        verbose_name_plural: 'Candidatos'
        ordering: [id]
