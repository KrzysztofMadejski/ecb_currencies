from rest_framework.views import APIView, Response
from .models import ExchangeRate
from .serializers import ConversionsSerializer

class ConversionsList(APIView):
    def get(self, request, format=None):
        """
        Returns a list of all available conversions
        """
        conversions = ExchangeRate.objects.values('target_currency', 'base_currency').distinct()

        serializer = ConversionsSerializer(conversions, many=True)
        return Response(serializer.data)
