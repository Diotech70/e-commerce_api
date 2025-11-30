from .views import CategoryView, ProductListView, ProductDetailView, ProductView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post/products/',ProductView,basename='post-product')
router.register(r'category/',CategoryView,basename='category')

urlpatterns =[path('',include(router.urls)),
              path('products/',ProductListView.as_view(),name='products'),
              path('<int:pk>/',ProductDetailView.as_view(),name='details'),
]
