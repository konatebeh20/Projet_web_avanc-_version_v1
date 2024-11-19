from api.models import Product
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from api.api.serializers import ProductSerializer1, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer1
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Product.objects.all()
    # route pour les produict avec un prix superieur a 500 
    @action(detail=False, methods=['GET'] , url_path='expensive-products', url_name='expensive_products')
    def expensive_products(self, request, *args, **kwargs):
        products = Product.objects.filter(price__gte=500)
        context = {'request': request}
        serializer = ProductSerializer1(products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def get_queryset(self):
        return super().get_queryset().filter(price__lte=500)