from django.shortcuts import get_object_or_404
from .models import User, Product, Sale, Role
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from uuid import uuid4

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #List all users
    def get_queryset(self):
            users = User.objects.all()
            return users
        
    #Get an user
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    #Create new user
    def create(self, request, *args, **kwargs):
        user_data = request.data
        id = uuid4()
        document = user_data['document']
        name = user_data['name']
        last_name = user_data['last_name']
        roles_id = Role(user_data['roles_id'])
        
        new_user = User.objects.create(id=id, document=document, name=name, 
                                       last_name=last_name, roles_id=roles_id)
        new_user.save()
        serializer = UserSerializer(new_user)
        return Response(serializer.data)
        
    #Delete user   
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response({'message': 'User has been deleted succesfully'})
   
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    #List all products
    def get_queryset(self):
        products = Product.objects.all()
        return products

    #Get a product 
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 
    
    #Create new product
    def create(self, request, *args, **kwargs):
        role_data = request.data
        id = uuid4()
        name = role_data['name']
        description = role_data['description']
        price = int(role_data['price'])
        
        new_product = Product.objects.create(id=id, name=name, description=description, price=price)
        new_product.save()
        serializer = ProductSerializer(new_product)
        return Response(serializer.data)

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    
    #List all Roles
    def get_queryset(self):
        roles = Role.objects.all()
        return roles

    #Get role by id
    def retrieve(self, request, pk=None):
        queryset = Role.objects.all()
        role = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data) 

    #Create new role
    def create(self, request, *args, **kwargs):
        role_data = request.data
        id = uuid4()
        name = role_data['name']
        
        new_role = Role.objects.create(id=id, name=name)
        new_role.save()
        serializer = RoleSerializer(new_role)
        return Response(serializer.data)
    
    #Delete a role
    def destroy(self, request, *args, **kwargs):
        role = self.get_object()
        role.delete()
        return Response({'message': 'Role has been deleted succesfully'})
    
class SaleViewSet(viewsets.ModelViewSet):
        serializer_class = SaleSerializer
        
        #List all sales
        def get_queryset(self):
            sales = Sale.objects.all()
            return sales
        
        #Create new sale
        def create(self, request, *args, **kwargs):
            now = datetime.now()
            dt_str = now.strftime("%Y-%m-%d %H:%M:%S")
            sale_data = request.data
            id = uuid4() #Generate new id for sale
            product_id = Product(sale_data['products_id'])
            qty = int(sale_data['qty'])
            sale_at = dt_str #Set datetime of sale
            user_id = User(sale_data['users_id'])
            
            new_sale = Sale.objects.create(id=id, products_id=product_id, qty=qty,
                                           sale_at=sale_at, users_id=user_id)
            new_sale.save()
            serializer = SaleSerializer(new_sale)
            return Response(serializer.data)
           
        def update(self, request, *args, **kwargs):
            pass
        
        #Delete a sale
        def destroy(self, request, *args, **kwargs):
            sale = self.get_object()
            sale.delete()
            return Response({'message': 'Sale has been deleted succesfully'})
        