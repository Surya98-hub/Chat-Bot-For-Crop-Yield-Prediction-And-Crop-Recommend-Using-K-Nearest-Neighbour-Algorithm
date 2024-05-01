from django.db import models
from django.contrib.auth.models import AbstractUser


class Bot(models.Model):
    user = models.TextField(max_length=200)
    bot = models.TextField(max_length=200)

    def __str__(self):
        return self.user, self.bot
    

class mylogin(AbstractUser):

    def __str__(self):
        return self.username
        







