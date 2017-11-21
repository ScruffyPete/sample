from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    advisers = models.ManyToManyField('Adviser')

    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klienci'

    def __str__(self):
        return self.name


class Adviser(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Doradca'
        verbose_name_plural = 'Doradcy'

    def __str__(self):
        return self.name
