from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    

