from atexit import register
from django.urls import include, path
from rest_framework import routers
from sales_api.models import Sale
from sales_api.views import ProductViewSet, RoleViewSet, UserViewSet, SaleViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'sales', SaleViewSet, basename='sales')

urlpatterns = [
    path('', include(router.urls))
]
