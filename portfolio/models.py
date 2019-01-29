from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100, verbose_name='titulo')
    description=models.TextField(verbose_name='descripcion')
    image=models.ImageField(upload_to='portafolio', verbose_name='imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='fecha actualización')
    urlfield=models.CharField(max_length=100, verbose_name='enlace', null=True, blank=True)
    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']

    def __str__(self):
        return self.title