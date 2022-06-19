from gc import get_objects
from rest_framework.permissions import AllowAny, BasePermission
from django.shortcuts import get_object_or_404
from .models import User, Product, Sale, Role
from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer, RoleSerializer, SaleSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
            users = User.objects.all()
            return users

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
        roles_id = Role(user_data['roles_id'])


        #Create new User
        new_user = User.objects.create(id=id, document=document, name=name, 
                                       last_name=last_name, roles_id=roles_id)
        new_user.save()
        
        serializer = UserSerializer(new_user)
        return Response(serializer.data)
        
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        products = Product.objects.all()
        return products

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

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    
    def get_queryset(self):
        roles = Role.objects.all()
        return roles

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
    
    def destroy(self, request, *args, **kwargs):
        role = self.get_object()
        role.delete()
        return Response({'message': 'Role was deleted succesfully'})
    
class SaleViewSet(viewsets.ModelViewSet):
    
        serializer_class = SaleSerializer
        
        def get_queryset(self):
            sales = Sale.objects.all()
            return sales