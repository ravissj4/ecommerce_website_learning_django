from django.db import models

# Create your models here.

class Product(models.Model):
    # id = models.IntegerField... # stored as default with autoincrement=True
    # blank = false means that the user cannot leave the field blank and submit the form
    # null = false means that the value in the database table cannot be null
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=29.99)
    
    # adding this field sale_price afterwards and hence cannot have null=False and blank=False
    # so, either make them true or have a default value 
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)

    slug = models.SlugField()
    
    # auto_now_add = True means that when an instance/object of Product is saved, 
    # its automatically doing to add the latest(now) timestamp
    # auto_now = True means that it'll update the timestamp whenever the object is updated
    # and saved in the database
    # for timestamp we want it to be just defined once when the product is first time created
    # for updated, we want the timestamp to keep on updating to the latest saved state of the 
    # object in the database !!!!
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    # requested_shipping = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

    
class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title
    