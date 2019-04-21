from django.http import Http404
from rest_framework.views import APIView, Response
from .models import ExchangeRate
from .serializers import ConversionsSerializer, RateHistorySerializer


class ConversionsList(APIView):
    def get(self, request, format=None):
        """
        Returns a list of all available conversions
        """
        conversions = ExchangeRate.objects.values('target_currency', 'base_currency').distinct()

        serializer = ConversionsSerializer(conversions, many=True)
        return Response(serializer.data)


class RateHistory(APIView):
    def get(self, request, base, target, format=None):
        """
        Returns all rates for a given conversion
        """
        rates = ExchangeRate.objects.filter(target_currency=target, base_currency=base).order_by('at')

        if not rates:
            raise Http404

        serializer = RateHistorySerializer(rates, many=True)
        return Response(serializer.data)
