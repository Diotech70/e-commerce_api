from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
      product_name =serializers.ReadOnlyField(source='product.name')
      product_price = serializers.ReadOnlyField(source='product.price')
      total_price = serializers.SerializerMethodField()
      class Meta:
            model = CartItem
            fields =['id','product','product_name','product_price','quantity','total_price']
      def get_total_price(self,obj):
          return obj.get_total_price()
