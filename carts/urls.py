from django.urls import path, include
from .views import CartListView, AddToCartView, UpdateCartView, RemoveCartView

urlpatterns =[path('',CartListView.as_view(),name='cart-list'),
               path('add/',AddToCartView.as_view(),name='add-cart'),
               path('update/<int:pk>/',UpdateCartView.as_view(),name='cart-update'),
               path('remove/<int:pk>/',RemoveCartView.as_view(),name='cart-remove'),
]
