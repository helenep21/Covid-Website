# Generated by Django 3.0.5 on 2020-05-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_auto_20200508_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
