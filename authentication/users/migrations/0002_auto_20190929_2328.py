# Generated by Django 2.2.5 on 2019-09-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
