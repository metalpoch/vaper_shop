from django.db import models
from django.contrib.auth.models import AbstractUser


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
