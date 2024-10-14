# Generated by Django 5.0 on 2024-02-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_glas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Best',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='index/img')),
                ('bio', models.TextField()),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
    ]
