# Generated by Django 3.1.3 on 2020-11-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cat', models.CharField(max_length=255, unique=True, verbose_name='Nombre categoria')),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_actual', models.DateField(auto_now=True)),
            ],
        ),
    ]
