from rest_framework import serializers
from .models import ExchangeRate


class ConversionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('target_currency', 'base_currency')


class RateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('rate', 'at')
