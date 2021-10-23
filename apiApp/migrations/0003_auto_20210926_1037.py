# Generated by Django 3.1.4 on 2021-09-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_blog_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(blank=True, choices=[('DRAFT', 'DRAFT'), ('IN-REVIEW', 'IN-REVIEW'), ('PUBLISHED', 'PUBLISHED')], default=1, max_length=10, null=True),
        ),
    ]
