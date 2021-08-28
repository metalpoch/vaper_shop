from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    # file will be uploaded to MEDIA_ROOT/uploads
    image = models.ImageField(upload_to='static/img/vaper/')

    def __str__(self):
        return f'ID {self.id}: {self.model} - {self.name}, stock: {self.stock}'


class Client(AbstractUser):
    gender = models.CharField(
        max_length=1,
        choices=[
            ('F', 'Female'),
            ('M', 'Male'),
        ],
    )
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    address = models.TextField()
    credits = models.FloatField(default=0)

    def __str__(self):
        return f'{self.username}: {self.first_name} {self.last_name}'


class SalesRecord(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.purchase_date} {self.client} bought {self.amount} \
            {self.product}'
