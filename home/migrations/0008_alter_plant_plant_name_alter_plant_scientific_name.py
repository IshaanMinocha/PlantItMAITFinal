# Generated by Django 4.1.4 on 2022-12-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_plant_medicinal_use_plant_plant_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='scientific_name',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
