from rest_framework import serializers
from .models import OrderItem, Order
from carts.serializers import CartItem

class OrderItemSerializer(serializers.ModelSerializer):
      product_name = serializers.ReadOnlyField(source='product.name')
      class Meta:
            model = OrderItem
            fields =['id','product','product_name','quantity','price']


class OrderSerializer(serializers.ModelField):
      items = OrderItemSerializer(many=True,read_only=True)
      class Meta:
            model = Order
            fields =['id','user','total_price','status','created','items']
            read_only_fields =['user','total_price','status','created','items']

