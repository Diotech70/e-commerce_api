from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryView(viewsets.ModelViewSet):
      serializer_class = CategorySerializer
      queryset = Category.objects.all()
      permission_classes =[permissions.AllowAny]

class ProductView(viewsets.ModelViewSet):
      serializer_class = ProductSerializer
      queryset = Product.objects.all()
      permission_classes =[permissions.AllowAny]

class ProductListView(generics.ListAPIView):
      serializer_class = ProductSerializer
      queryset = Product.objects.all()

class ProductDetailView(generics.RetrieveAPIView):
      serializer_class = ProductSerializer
      queryset = Product.objects.all()
# Create your views here.
