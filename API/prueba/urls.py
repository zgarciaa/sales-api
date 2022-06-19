from django.urls import include, path
from rest_framework import routers
from sales_api import views
from sales_api.models import Role, Product
from sales_api.serializers import RoleSerializer, ProductSerializer

router = routers.DefaultRouter()
router.register(r'users_list', views.UserViewSet)
#router.register(r'roles', views.RoleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('roles_list/', views.RoleList.as_view(queryset=Role.objects.all(), serializer_class=RoleSerializer), name='role-list'),
    path('products_list/', views.ProductList.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer), name='product-list')
]
