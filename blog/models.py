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
    title = models.CharField(max_length=50, db_index=True, blank=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category_phone_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Category_a_laptop(models.Model):
    catalog_category_a_laptop = models.ManyToManyField('Catalog',
                                                       blank=True,
                                                       related_name='category_a_laptop_catalog')
    title = models.CharField(max_length=50, db_index=True, blank=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('category_a_laptop_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# ========================= Product ==================================


class Product_Phone(models.Model):
    product_phone_catalog = models.ManyToManyField(
        'Catalog', blank=True, related_name='catalog_product_phone')
    product_phone_category = models.ManyToManyField(
        'Category_Phone', blank=True, related_name='category_product_phone')
    title = models.CharField(max_length=50, db_index=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(db_index=True, upload_to=media)
    camera = models.CharField(
        max_length=50, db_index=True, blank=True)  # камера
    memory = models.CharField(
        max_length=50, db_index=True, blank=True)  # память
    thach_id = models.CharField(
        max_length=50, db_index=True, blank=True)  # отпечаток
    cairt_sim = models.CharField(
        max_length=50, db_index=True, blank=True)  # сим карта
    accessory = models.CharField(
        max_length=50, db_index=True, blank=True)  # почие аксисуары
    decimal = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True)  # цена

    def get_absolute_url(self):
        return reverse('product_phone_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Product_a_laptop(models.Model):
    product_a_laptop_catalog = models.ManyToManyField('Catalog',
                                                      blank=True,
                                                      related_name='catalog_product_a_laptop')
    product_a_laptop_category = models.ManyToManyField('Category_a_laptop',
                                                       blank=True,
                                                       related_name='category_product_a_laptop')
    title = models.CharField(max_length=50, db_index=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(db_index=True, upload_to=media)
    weight = models.CharField(max_length=30, db_index=True, blank=True)  # вес
    memory = models.CharField(
        max_length=30, db_index=True, blank=True)  # память
    ssd = models.CharField(max_length=30, db_index=True,
                           blank=True)  # SSD‑накопитель до 1,5 ТБ
    touch = models.CharField(
        max_length=30, db_index=True, blank=True)  # Touch ID
    accessory = models.CharField(
        max_length=50, db_index=True, blank=True)  # почие аксисуары
    decimal = models.DecimalField(max_digits=6, decimal_places=3, blank=True)

    def get_absolute_url(self):
        return reverse('product_a_laptop_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
