from django.db import models


class User(models.Model):
    username = models.CharField('Имя пользователя', max_length=255)
    email = models.CharField('E-mail пользователя', max_length=255)
    password = models.CharField('Пароль пользователя', max_length=255)

    def __str__(self):
        return self.username