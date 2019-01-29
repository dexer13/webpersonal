from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class InformacionPersonal(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion=RichTextField(default='No hay descripción')
    hab_blandas=RichTextField(default='No hay habilidades blandas')
    hab_tecnicas=RichTextField(default='No hay habilidades técnicas')
    link_facebook=models.URLField(null=True, blank=True)
    link_instagram=models.URLField(null=True, blank=True)
    link_github=models.URLField(null=True, blank=True)
    foto=models.ImageField(upload_to='perfil', null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username