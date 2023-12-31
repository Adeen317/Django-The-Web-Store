#Database
from django.contrib.auth.models import User #To call user from django
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)


    #For changing category name to plural and ordering
    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    #Naming the items in categories
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

     #Naming the items in categories
    def __str__(self):
        return self.name