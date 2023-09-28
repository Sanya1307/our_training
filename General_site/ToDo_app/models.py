from django.db import models

class Model_Memory(models.Model):
    topic = models.CharField('Тема', max_length=100)
    time = models.DateField('Дата напоминания')

    def __str__(self):
        return self.topic

