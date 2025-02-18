from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='аватар')

    class Meta:
        db_table = 'user'
        verbose_name = 'користувач'
        verbose_name_plural = 'користувачі'


    def __str__(self):
        return self.username