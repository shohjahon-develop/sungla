from django.db import models
from django.urls import reverse


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("aboutsDetail", args=[self.slug])


class Glas(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=300)
    price = models.IntegerField()

    def get_absolute_url(self):
        return reverse("glassDetail", args=[self.slug])

    def __str__(self):
        return self.name


class Best(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    bio = models.TextField()
    slug = models.SlugField(max_length=300)


    def get_absolute_url(self):
        return reverse("bestsDetail", args=[self.slug])

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=300)
    number  = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Abouts(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='about/img')
    slug = models.SlugField(max_length=300)
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse("aboutsDetail",args=[self.slug])

    def __str__(self):
        return self.name















































































































