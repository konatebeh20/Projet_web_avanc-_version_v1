from api.models import Product
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    author_products = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'author_products']
        
        
    def get_author_products(self, obj):
        products = obj.product_set.all()
        context = self.context
        return ProductSerializer2(products, many=True, context=context).data


class ProductSerializer1(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(max_length=255)
    price_in_euros = serializers.SerializerMethodField()
    description_in_euros = serializers.SerializerMethodField()
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    #author = UserSerializer()
    class Meta:
        model = Product
        fields = "__all__"
        #excludes = ['created_at', 'updated_at']
    
    
    def get_price_in_euros(self, obj): # get_<field_name>
        return obj.get_price_in_euros()
    
    def get_description_in_euros(self, obj):
        return obj.get_description()
    
  
   

    def validate_name(self, value): # validate_<field_name>  clean_<field_name>
        if value in ['konate', 'beh', 'konate beh']:
            raise serializers.ValidationError('You are not allowed to use this name')
        return value    
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        print('email:', email)
        # connected user 
        user = self.context['request'].user
        print('user:', user)
        validated_data['author'] = user
        return super().create(validated_data)    
        
        
class ProductSerializer2(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='api:product_api_view_detail', lookup_field='pk')
    class Meta:
        model = Product
        fields = ['name', 'price', 'link']
        #excludes = ['created_at', 'updated_at']
    

  
