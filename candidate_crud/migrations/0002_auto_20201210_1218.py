# Generated by Django 3.1.4 on 2020-12-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='portrait_img',
            field=models.CharField(max_length=255, verbose_name='Imagen'),
        ),
    ]
