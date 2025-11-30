from django.shortcuts import render
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from carts.models import CartItem
from rest_framework import generics, permissions, status

class CreateOrderView(generics.CreateAPIView):
      serializer_class = OrderSerializer
      permission_claasses =[permissions.IsAuthenticated]
      def post(self,request,*args,**kwargs):
          cart_items = CartItem.objects.filter(user=request.user)
          if not cart_items.exists():
             return Responser({'detail':'cart is empty'},status=400)
          total =sum([item.get_total_price() for item in cart_items])
          order = Order.objects.create(user=request.user,total_price=total)
          for item in cart_items:
              OrderItem.objects.create(order=order,product=item.product,quantity=item.quantity,price=item.product.price)
          cart_items.delete()
          serializer = OrderSerializer(order)
          return Response(serializer.data,status=201)

class OrderListView(generics.ListAPIView):
      serializer_class = OrderSerializer
      permission_classes =[permissions.IsAuthenticated]
      def get_queryset(self):
          return Order.objects.filter(user=self.request.user)

class OrderPayView(generics.GenericAPIView):
      serializer_class = OrderSerializer
      permission_classes =[permissions.IsAuthenticated]
      def post(self,request,pk):
          order = Order.objects.get(id=pk,user=request.user)
          order.status = 'paid'
          order.save()
          serializer = OrderSerializer(order)
          return Response(serializer.data)
# Create your views here.
