# Generated by Django 2.1.4 on 2019-01-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190127_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionpersonal',
            name='foto',
            field=models.ImageField(null=True, upload_to='perfil'),
        ),
    ]
