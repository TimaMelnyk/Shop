from __future__ import unicode_literals
from django.db import models
from datetime import *
from django import forms

USER = 'USER'

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of category')
    alias = models.SlugField(verbose_name='Alias category')
     
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return 'Category %s' % self.name

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product name')
    price = models.IntegerField(default=0, verbose_name='Price')
    image = models.CharField(max_length=255, verbose_name='Reference on the image')
    alias = models.SlugField(verbose_name='Alias product')
    
    category = models.ForeignKey(Category)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return 'Product %s' % self.name
# 
# class User(models.Model):
#     login = models.CharField(max_length=20,null=True)
#     password = models.CharField(max_length=20,null=True)
#     phoneNumber = models.CharField(max_length=15, null=True)

class User(models.Model):
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    login = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)
    phoneNumber = models.CharField(max_length=15, null=True)
    vkId = models.CharField(max_length=15,null=True)
    permissions = models.CharField(max_length=20, default=USER)

    @property
    def isAdmin(self):
        return self.permissions == ADMIN


class Zakaz(models.Model):
    name = models.CharField(max_length=255, verbose_name='Purchaser')
    phone = models.CharField(max_length=255, verbose_name='Phone')
    zakaz = models.CharField(max_length=255, verbose_name='Things')
    summa = models.ImageField(default=0, verbose_name="Amount")
    date = models.DateTimeField(default=datetime.now(),verbose_name="Time")
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        
    def __str__(self):
        return 'Order  %s' % self.name
