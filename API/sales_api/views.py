from rest_framework.permissions import AllowAny, BasePermission
from django.shortcuts import get_object_or_404
from .models import User, Product, Sale, Role
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer, RoleSerializer
from sales_api import serializers

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        user_data = request.data
        id = user_data['id']
        document = user_data['document']
        name = user_data['name']
        last_name = user_data['last_name']
        roles_id = user_data['roles_id']
        
        #Create new User
        new_user = User.objects.create(id=id, document=document, name=name, 
                                       last_name=last_name, roles_id=roles_id)
        new_user.save()
        
        serializer = ProductSerializer(new_user)
        return Response(serializer.data)
        
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)  
    
    def create(self, request, *args, **kwargs):
        role_data = request.data
        id = role_data['id']
        name = role_data['name']
        description = role_data['description']
        price = role_data['price']
        
        #Create new product
        new_product = Product.objects.create(id=id, name=name, description=description, price=price)
        new_product.save()
        
        serializer = ProductSerializer(new_product)
        return Response(serializer.data)
    
class RoleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Role.objects.all()
        role = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data) 

    def create(self, request, *args, **kwargs):
        role_data = request.data
        id = role_data['id']
        name = role_data['name']
        
        #Create new Role
        new_role = Role.objects.create(id=id, name=name)
        new_role.save()
        
        serializer = RoleSerializer(new_role)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        queryset = Role.objects.all()
        print(pk)
        role = get_object_or_404(queryset, pk=pk)
        role.delete()
        return Response({'message':'Role has been deleted'})