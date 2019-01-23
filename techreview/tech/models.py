from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# producttype, product, review

class ProductType(models.Model):
    typename = models.CharField(max_length = 255)
    typedescription = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'producttype'

class Product(models.Model):
    productname = models.CharField(max_length = 255)
    producttype = models.ForeignKey(ProductType, on_delete = models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    productentrydate = models.DateField()
    producturl = models.URLField(null = True, blank = True)
    productdescription = models.TextField()

    def __str__(self):
        return self.productname

    class Meta:
        db_table = 'product'

class Review(models.Model):
    reviewtitle = models.CharField(max_length = 255)
    reviewdate = models.DateField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ManyToManyField(User)
    reviewrating = models.SmallIntegerField()
    reviewtext = models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table = 'review'
