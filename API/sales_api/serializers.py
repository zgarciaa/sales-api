from rest_framework import serializers
from .models import Role, User, Product, Sale

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','document', 'name', 'last_name', 'roles_id')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','name', 'description', 'price')
        
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields=('id', 'product_id', 'qty', 'sale_at', 'users_id')
        

        
