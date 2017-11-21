from django import forms
from django.db.models import Q

from clients.models import Adviser
from offers.models import Offer
from utils.mixins import SearchFormMixin


class ClientSearchForm(SearchFormMixin, forms.Form):
    name = forms.CharField(required=False)
    offer = forms.ModelChoiceField(queryset=Offer.objects.all(), required=False)
    adviser = forms.ModelChoiceField(queryset=Adviser.objects.all(), required=False)

    def search_name(self, value):
        return Q(name__icontains=value)

    def search_offer(self, value):
        return Q(offer=value)

    def search_adviser(self, value):
        return Q(pk__in=value.client_set.values('pk'))
