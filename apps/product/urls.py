from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]