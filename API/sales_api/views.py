#from django.contrib.auth.models import User, Group
from msilib.schema import ListView
from rest_framework import generics

from django import views
from .models import User, Product, Sale, Role
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, ProductSerializer, RoleSerializer

class AddRoleViewSet(viewsets.ModelViewSet):
    pass
              
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = UserSerializer
    
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
