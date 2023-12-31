from django.contrib import admin

#Registering it into Admin Interface Django Administration
from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)

# Register your models here.
