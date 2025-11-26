from django.db import models
from django.contrib import admin
class Author(models.Model):
    name = models.CharField(max_length=100,help_text="Enter the author's name")
    bith_date = models.DateField()
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','bith_date')

