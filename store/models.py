from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    in_stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    available = models.BooleanField(default=True)


    class Meta:
        verbose_name = verbose_name_plural = 'Product'
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'product_id': self.slug})


class Category(models.Model):
    category_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_details', kwargs={'category_id': self.slug})
