from django.urls import path
from .views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns =[path('register/',RegisterView.as_view(),name='register'),
              path('profile/',UserView.as_view(),name='profile'),
              path('token/',TokenObtainPairView.as_view(),name='token'),
              path('token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
]
