# Generated by Django 3.1.4 on 2021-09-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sub_category',
            field=models.ManyToManyField(to='apiApp.SubCategory'),
        ),
    ]
