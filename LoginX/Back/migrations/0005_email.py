# Generated by Django 2.1.2 on 2018-11-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0004_auto_20181104_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
