from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.

def media(instance, filename):
    image = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, image)


class Catalog(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(db_index=True, upload_to=media)

    def get_absolute_url(self):
        return reverse('catalog_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# ==================== Category =================================
class Category_Phone(models.Model):
    catalog_category_phone = models.ManyToManyField('Catalog',
                                              blank=True,
                                              related_name='category_phone_catalog')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category_phone_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

class Category_a_laptop(models.Model):
    catalog_category_a_laptop = models.ManyToManyField('Catalog',
                                              blank=True,
                                              related_name='category_a_laptop_catalog')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category_a_laptop_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# ========================= Product ==================================
class Product_Phone(models.Model):
    phone_catalog = models.ManyToManyField('Catalog', blank=True, related_name='catalog_phone')
    phone_category = models.ManyToManyField('Category', blank=True, related_name='category_phone')
    title = models.CharField(max_length=50, db_index=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(db_index=True, upload_to=media)
    camera = models.CharField(max_length=50, db_index=True, blank=True) # камера
    memory = models.CharField(max_length=50, db_index=True, blank=True) # память
    thach_id = models.CharField(max_length=50, db_index=True, blank=True) # отпечаток
    cairt_sim = models.CharField(max_length=50, db_index=True, blank=True) # сим карта
    decimal = models.DecimalField(max_digits=6, decimal_places=3, blank=True) # цена

    def __str__(self):
        return self.title