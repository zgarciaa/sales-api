from django.shortcuts import get_object_or_404
from .models import User, Product, Sale, Role
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from uuid import uuid4

ID_ROLES = {
    'admin': '796cd220-3b4f-4b90-9bd6-0fa695979ddf',
    'employee': '5935287c-a160-4c1e-bbfa-4169b943f4e8'
}

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #List all users
    def get_queryset(self):
            users = User.objects.all()
            return users
                   
    #Get an user
    def retrieve(self, request, pk=None):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    #Create new user
    def create(self, request, *args, **kwargs):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        
        user_data = request.data
        id = user_data['id']
        document = user_data['document']
        name = user_data['name']
        last_name = user_data['last_name']
        role = user_data['roles_id']
        roles_id = Role(role)
        
        new_user = User.objects.create(id=id, document=document, name=name, 
                                       last_name=last_name, roles_id=roles_id)
        new_user.save()
        return Response('User created succesfully', status.HTTP_201_CREATED)
        
    #Delete user   
    def destroy(self, request, *args, **kwargs):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        
        user = self.get_object()
        user.delete()
        return Response('User deleted succesfully', status.HTTP_200_OK)
   
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    #List all products
    def get_queryset(self):
        products = Product.objects.all()
        return products

    #Get a product 
    def retrieve(self, request, pk=None):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin'] and hdrs != ID_ROLES['employee']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data) 
    
    #Create new product
    def create(self, request, *args, **kwargs):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        
        product_data = request.data
        id = product_data['id']
        name = product_data['name']
        description = product_data['description']
        price = int(product_data['price'])
        
        new_product = Product.objects.create(id=id, name=name, description=description, price=price)
        new_product.save()
        return Response('Product created succesfully', status.HTTP_201_CREATED)

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    
    #List all Roles
    def get_queryset(self):
        roles = Role.objects.all()
        return roles

    #Get role by id
    def retrieve(self, request, pk=None):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        queryset = Role.objects.all()
        role = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data) 

    #Create new role
    def create(self, request, *args, **kwargs):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        product_data = request.data
        id = uuid4()
        name = product_data['name']
        new_role = Role.objects.create(id=id, name=name)
        new_role.save()
        return Response('Role created succesfully', status.HTTP_201_CREATED)
    
    #Delete a role
    def destroy(self, request, *args, **kwargs):
        hdrs = request.headers.get('Auth')
        #Check if user is authorized
        if hdrs != ID_ROLES['admin']:
            return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
        role = self.get_object()
        role.delete()
        return Response('Role deleted succesfully', status.HTTP_200_OK)
    
class SaleViewSet(viewsets.ModelViewSet):
        serializer_class = SaleSerializer
        
        def get_queryset(self):
            sales = Sale.objects.order_by('-sale_at')
            return sales
        
        def retrieve(self, request, *args, **kwargs):
            hdrs = request.headers.get('Auth')
            #Check if user is authorized
            if (hdrs != ID_ROLES['admin'] and hdrs != ID_ROLES['employee']):
                return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
            sales = self.get_object()
            serializers = self.get_serializer(sales)
            return Response(serializers.data)
        
        #Create new sale
        def create(self, request, *args, **kwargs):
            hdrs = request.headers.get('Auth')
            #Check if user is authorized
            if (hdrs != ID_ROLES['admin'] and hdrs != ID_ROLES['employee']):
                return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
            
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
            return Response('Sale created succesfully', status=status.HTTP_201_CREATED)
           
        #Update a sale
        def update(self, request, *args, **kwargs):
            hdrs = request.headers.get('Auth')
            #Check if user is authorized
            if hdrs != ID_ROLES['admin']:
                return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response('Sale updated succesfully', status=status.HTTP_200_OK)
        
        #Delete a sale
        def destroy(self, request, *args, **kwargs):
            hdrs = request.headers.get('Auth')
            #Check if user is authorized
            if hdrs != ID_ROLES['admin']:
                return Response('User is not authorized', status.HTTP_401_UNAUTHORIZED)
            
            sale = self.get_object()
            sale.delete()
            return Response('Sale deleted succesfully', status=status.HTTP_200_OK)
        
class SalesOfDayViewSet(viewsets.ModelViewSet):
    pass