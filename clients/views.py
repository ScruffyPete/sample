from rest_framework import viewsets

from clients.forms import ClientSearchForm
from clients.models import Client
from clients.serializers import ClientSerializer
from utils.backends import SearchFilter


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_form_class = ClientSearchForm
    queryset = Client.objects.prefetch_related('offer_set', 'advisers')
