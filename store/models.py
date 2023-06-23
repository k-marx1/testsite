from django.db import models
from django.conf import settings
from decimal import Decimal
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    in_stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})

    def discount_price(self):
        return round(self.price - self.price * Decimal.from_float(self.discount), 2)

    def image_value_error_handler(self):
        if self.photo:
            return self.photo.url
        else:
            return None


class Category(models.Model):
    category_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_details', kwargs={'category_id': self.slug})



