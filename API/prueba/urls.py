from django.urls import include, path
from rest_framework import routers
from sales_api.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'sales_report', SaleReportViewSet, basename='sales_report')

urlpatterns = [
    path('', include(router.urls))
]