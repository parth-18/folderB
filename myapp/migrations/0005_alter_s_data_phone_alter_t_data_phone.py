# Generated by Django 4.0.2 on 2022-03-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_data',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='t_data',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
