# Generated by Django 2.2.5 on 2019-09-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190929_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='group',
            field=models.CharField(default='Contactos', max_length=20),
        ),
    ]
