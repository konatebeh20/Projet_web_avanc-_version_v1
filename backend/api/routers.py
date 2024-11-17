from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.api.viewset import ProductViewSet

"""
defaut router est utilisé pour les opérations CRUD
par contre simple router est utilisé pour  les seules opérations de lecture
"""

router = DefaultRouter()
router.register('v1/product', ProductViewSet, basename='product')

urlpatterns = router.urls