from django.db import models
from django.conf import settings
from product.models import Product
from carts.models import CartItem

class Order(models.Model):
      STATUS_CHOICE = (('pending','pending'),('paid','paid'),('delivered','delivered'),)
      user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
      total_price = models.DecimalField(max_digits=10,decimal_places=2)
      status = models.CharField(max_length=100,choices=STATUS_CHOICE,default='pending')
      created = models.DateTimeField(auto_now_add=True)
      def __str__(self):
          return f'Order {self.id} by {self.user.username}'

class OrderItem(models.Model):
      order = models.ForeignKey(Order,on_delete=models.CASCADE)
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      quatity = models.PositiveIntegerField()
      price = models.DecimalField(max_digits=10,decimal_places=2)
      def __str__(self):
          return f'{self.poduct.name} ({self.quantity})'
# Create your models here.
