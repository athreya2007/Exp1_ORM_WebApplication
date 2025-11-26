# Ex01 Django ORM Web Application
## Date: 26.11.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class Author(models.Model):
    name = models.CharField(max_length=100,help_text="Enter the author's name")
    bith_date = models.DateField()
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','bith_date')


admins.py

from django.contrib import admin
from .models import Author, AuthorAdmin
admin.site.register(Author, AuthorAdmin)

```
## OUTPUT
![alt text](<Screenshot (112).png>)
![alt text](<Screenshot (113).png>)
![alt text](<Screenshot (111).png>)
## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
