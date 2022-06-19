from rest_framework.routers import DefaultRouter
from sales_api.views import ProductViewSet, RoleViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'roles', RoleViewSet, basename='roles')
urlpatterns = router.urls
