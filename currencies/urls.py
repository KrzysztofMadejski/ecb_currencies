from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ConversionsList

app_name = 'currencies-v1'
urlpatterns = [
    path('conversions', ConversionsList.as_view(), name='conversions-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
