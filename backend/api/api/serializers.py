from api.models import Product
from rest_framework import serializers

class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(max_length=255)
    price_in_euros = serializers.SerializerMethodField()
    description_in_euros = serializers.SerializerMethodField()
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    class Meta:
        model = Product
        fields = ['id', 'name', 'email', 'price_in_euros', 'description_in_euros', 'link']
        #excludes = ['created_at', 'updated_at']
    
    
    def get_price_in_euros(self, obj): # get_<field_name>
        return obj.get_price_in_euros()
    
    def get_description_in_euros(self, obj):
        return obj.get_description()
    
  
   

    def validate_name(self, value): # validate_<field_name>  clean_<field_name>
        if value in ['donald', 'trump', 'donald trump']:
            raise serializers.ValidationError('You are not allowed to use this name')
        return value    
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        print('email:', email)
        return super().create(validated_data)    
        
        
class ProductSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
  