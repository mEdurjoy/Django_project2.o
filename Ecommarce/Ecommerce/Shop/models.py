from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICE_KORO = (
    ('L', 'Lehenga'),
    ('S', 'Saree'),
    ('G', 'Gents pant'),
    ('BK', 'Borka'),
    ('BF', 'Baby Fashion'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    catagory = models.CharField(choices=CHOICE_KORO, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
    