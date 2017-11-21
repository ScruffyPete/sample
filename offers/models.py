from django.db import models


class Offer(models.Model):
    client = models.ForeignKey('clients.Client')
    create_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Oferty'

    def __str__(self):
        return 'Oferta klienta {} dodana {}'.format(self.client, self.create_date)
