from django.db import models

class phone_book(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50,null=True,blank=False)
    Phone_Number = models.CharField(max_length=50,null=True,blank=False)
