from api.models import Product
from api.api.serializers import ProductSerializer1 
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView



class ProductListApiView(ListModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer1
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class ProductDetailApiView(RetrieveModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer1
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    
class ProductCreateApiView(CreateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer1
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    
    

class ProductUpdateApiView(UpdateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer1
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)   
    
    
class ProductDeleteApiView(DestroyModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer1
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ProductRetrieveListApiView(RetrieveModelMixin, ListModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer1
    
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

class CombineApiViewSet(
    ProductRetrieveListApiView,
    ProductDetailApiView,
    ProductCreateApiView,
    ProductUpdateApiView,
    ProductDeleteApiView
    ):
    pass
   


class CombineReadOnlyApiViewSet(
    ProductRetrieveListApiView,
    ):
    pass    
