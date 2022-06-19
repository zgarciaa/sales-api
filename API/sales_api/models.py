from django.db import models

class Role(models.Model):
    id = models.UUIDField(primary_key=True) # UUID
    name = models.CharField(max_length=30)

class User(models.Model):
    id = models.UUIDField(primary_key=True) # UUID
    document = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roles_id = models.ForeignKey(to=Role, on_delete=models.CASCADE) # UUID
      
class Product(models.Model):
    id = models.UUIDField(primary_key=True) # UUID
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.IntegerField() 
    
class Sale(models.Model):
    id = models.UUIDField(primary_key=True) # UUID
    products_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    sale_at = models.DateTimeField()
    users_id = models.ForeignKey(to=User, on_delete=models.CASCADE) # UUID

