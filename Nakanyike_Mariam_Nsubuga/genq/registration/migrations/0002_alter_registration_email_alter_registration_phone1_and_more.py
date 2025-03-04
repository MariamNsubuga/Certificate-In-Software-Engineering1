# Generated by Django 4.2 on 2023-04-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
