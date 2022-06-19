#from django.contrib.auth.models import User, Group
from .models import User, Product, Sale, Role
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, ProductSerializer, RoleSerializer
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class AddRoleViewSet(viewsets.ModelViewSet):
    def addRoles():
        con = psycopg2.connect(
        database="store", 
        user="postgres", 
        password="bthemounim1",
        host="localhost"
        )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # Autocommit
        cursor = con.cursor()
        
        #Add new Role
        ssql = """INSERT INTO sales_api_role (id, name) 
                     VALUES ('2c13e2e0-ef83-11ec-8ea0-0242ac120002', 'admin'),
                            ('5831f790-ef83-11ec-8ea0-0242ac120002','employee'),
                            ('607ed0c6-ef83-11ec-8ea0-0242ac120002','everyone');"""
        try:
            cursor.execute(ssql)
            print("Product added successfully")
        except Exception as e:
            print(e)
        finally:
            # Closing database connection.
            if con:
                cursor.close()
                con.close()
                print("PostgreSQL connection is closed")
    addRoles() 
              
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
