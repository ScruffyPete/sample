from rest_framework import serializers

from clients.models import Client, Adviser
from offers.models import Offer


class AdviserNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adviser
        fields = ['id', 'name']


class OfferNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ['id', 'create_date']


class ClientSerializer(serializers.ModelSerializer):
    offer_set = OfferNestedSerializer(many=True, read_only=True)
    advisers = AdviserNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
