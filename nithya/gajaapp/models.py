from django.db import models
from django.contrib import admin 
class Bankloan(models.Model):
   Name =models.CharField(max_length =20)
   Accountno =models.IntegerField(primary_key="accountno") 
   Mobileno =models.IntegerField()
   Loanamount =models.IntegerField()
   Branch =models.CharField(max_length =21)

class BankloanAdmin(admin.ModelAdmin):
  list_display=('Name','Accountno','Mobileno','Loanamount','Branch')



