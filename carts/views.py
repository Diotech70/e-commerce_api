from django.shortcuts import render
from .serializers import CartItemSerializer
from .models import CartItem
from rest_framework import generics, permissions
from product.models import Product
from rest_framework.response import Response

class CartListView(generics.ListAPIView):
      serializer_class = CartItemSerializer
      permission_classes =[permissions.IsAuthenticated]
      def get_queryset(self):
          return CartItem.objects.filter(user=self.request.user)

class AddToCartView(generics.CreateAPIView):
      serializer_class = CartItemSerializer
      permission_classes =[permissions.IsAuthenticated]
      def post(self,request,*args,**kwargs):
          product_id = request.data.get('product')
          quantity = request.data.get('quantity')
          product = Product.objects.get(id=product_id)
          cart_item,created = CartItem.objects.get_or_create(user=request.user,product=product)
          if not created:
             cart_item.quantity += int(quantity)
             cart.save()
          serializer = CartItemSerializer(cart_item)
          return Response(serializer.data,status=status.HTTP_201_CREATED)

class UpdateCartView(generics.UpdateAPIView):
      serializer_class = CartItemSerializer
      permission_classes =[permissions.IsAuthenticated]
      queryset = CartItem.objects.all()
      def get_object(self):
          return CartItem.objects.get(id=self.kwargs['pk'],user=self.request.user)

class RemoveCartView(generics.DestroyAPIView):
      serializer_class = CartItemSerializer
      permission_classes =[permissions.IsAuthenticated]
      queryset = CartItem.objects.all()
      def get_object(self):
          return CartItem.objects.get(id=self.kwargs['pk'],user=self.request.user)

# Create your views here.
