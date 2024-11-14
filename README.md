# Ex02 Django ORM Web Application
## Date:14/11/2024
## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Untitled Diagram.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

models.py

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

```


## OUTPUT
![alt text](<Screenshot (11)-1.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
