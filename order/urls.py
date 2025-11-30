from django.urls import path
from .views import OrderListView, CreateOrderView, OrderPayView

urlpatterns =[path('create/',CreateOrderView.as_view(),name='create-order'),
              path('',OrderListView.as_view(),name='list-order'),
              path('<int:pk>/pay/',OrderPayView.as_view(),name='pay-order'),
]
