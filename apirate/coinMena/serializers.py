from django.db.models import fields
from rest_framework import serializers
from .models import ExchangeRate

class ExchangeRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExchangeRate
        fields = ['exchange_rate']