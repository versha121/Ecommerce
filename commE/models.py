from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=12)
    role=models.CharField(max_length=20)

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField('image',null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1, null=False,blank=False)         
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    card_holder_name = models.CharField(max_length=100)
    card_expiration_date = models.CharField(max_length=10)
    card_cvv = models.CharField(max_length=4)
    total_price = models.FloatField(null=True)
    payment_mode = models.CharField(max_length=50,null=False)
    payment_id = models.CharField(max_length=200, null=True)
    orderstatus =(
        ('pending','pending'),
        ('out for shipping','out for shipping'),
        ('completed','completed')
    )
    status=models.CharField(max_length=50, choices=orderstatus,default = 'pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=50,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} | {}'.format(self.id,self.tracking_no)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id,self.order.tracking_no)










    



#sharma coders
