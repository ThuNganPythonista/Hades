from django.db import models

# Create your models here.

class Categories(models.Model):
    categories = models.CharField(default="",max_length=50)
    def __str__(self):
        return self.categories

class Size(models.Model):
    size = models.CharField(default='', max_length=2)
    def __str__ (self):
        return self.size

class Items(models.Model):
    yellow = 'Yellow'
    green = 'Green'
    color_choice = (
        (yellow, 'mau vang'),
        (green, 'mau xanh'),
    )
    title = models.CharField(max_length=50)
    price = models.FloatField(default=50,max_length=50)
    code = models.CharField(default=50,max_length=11)
    discount = models.IntegerField(default=5, max_length=80)
    color = models.CharField(default=green,max_length=20,choices=color_choice)
    description = models.TextField(default=50,max_length=1000)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    categories= models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Img(models.Model):
    img = models.ImageField(upload_to='container-img')
    product = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title









