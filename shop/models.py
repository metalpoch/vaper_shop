from django.db import models
from clients.models import Client


class Product(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    # file will be uploaded to MEDIA_ROOT/uploads
    image = models.ImageField(upload_to='static/img/vaper/')

    def __str__(self):
        return f'ID {self.id}: {self.model} - {self.name}, stock: {self.stock}'


class SalesRecord(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.purchase_date} {self.client} bought {self.amount} \
            {self.product}'
