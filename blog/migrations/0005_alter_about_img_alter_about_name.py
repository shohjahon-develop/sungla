# Generated by Django 5.0 on 2024-02-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img',
            field=models.ImageField(upload_to='about/img'),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]