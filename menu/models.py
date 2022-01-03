from django.db import models

# Create your models here.

class Breakfast(models.Model): 
  food_pic = models.ImageField(upload_to=None, null=True,blank=True) 
  food=models.CharField(max_length=50)
  price=models.IntegerField(default=0)
  description=models.TextField(max_length=200)

  def __str__(self):
    return self.food
   
class Starter(models.Model): 
  food_pic = models.ImageField(upload_to=None, null=True,blank=True) 
  food=models.CharField(max_length=50) 
  food=models.CharField(max_length=50)
  price=models.IntegerField(default=0)
  description=models.TextField(max_length=200)

  def __str__(self):
    return self.food

class LunchDinner(models.Model):  
  food_pic = models.ImageField(upload_to=None, null=True,blank=True) 
  food=models.CharField(max_length=50)
  food=models.CharField(max_length=50)
  price=models.IntegerField(default=0)
  description=models.TextField(max_length=200)

  def __str__(self):
    return self.food
   
class Salad(models.Model):  
  food_pic = models.ImageField(upload_to=None, null=True,blank=True) 
  food=models.CharField(max_length=50)
  food=models.CharField(max_length=50)
  price=models.IntegerField(default=0)
  description=models.TextField(max_length=200)

  def __str__(self):
    return self.food
   
class Drink(models.Model):  
  food_pic = models.ImageField(upload_to=None, null=True,blank=True) 
  food=models.CharField(max_length=50)
  food=models.CharField(max_length=50)
  price=models.IntegerField(default=0)
  description=models.TextField(max_length=200)

  def __str__(self):
    return self.food
   
   
   