# Generated by Django 3.1.4 on 2020-12-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='prov_name',
        ),
        migrations.AddField(
            model_name='cv',
            name='address',
            field=models.CharField(default=None, max_length=255, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='cv',
            name='birth_date',
            field=models.DateField(default=None, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='cv',
            name='cv_txt',
            field=models.TextField(default=None, verbose_name='CV en texto'),
        ),
        migrations.AddField(
            model_name='cv',
            name='dni',
            field=models.CharField(default=None, max_length=255, verbose_name='DNI'),
        ),
        migrations.AddField(
            model_name='cv',
            name='mobile',
            field=models.CharField(default=None, max_length=255, verbose_name='Mobil'),
        ),
        migrations.AddField(
            model_name='cv',
            name='portrait_img',
            field=models.CharField(default=None, max_length=255, verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='cv',
            name='telephone',
            field=models.CharField(default=None, max_length=255, verbose_name='Telefono fijo'),
        ),
    ]
