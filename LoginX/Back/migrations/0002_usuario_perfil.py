# Generated by Django 2.1.2 on 2018-10-31 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default='Administrador', max_length=20),
        ),
    ]