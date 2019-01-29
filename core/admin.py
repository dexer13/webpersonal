from django.contrib import admin
from .models import InformacionPersonal

# Register your models here.
class InformacionPersonalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(InformacionPersonal, InformacionPersonalAdmin)
