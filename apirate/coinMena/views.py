from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from apirate.coinMena.fetch_rate import fetch_rate
from apirate.coinMena.models import ExchangeRate
from .serializers import ExchangeRateSerializer
from rest_framework.views import APIView
from apirate.coinMena import serializers
from rest_framework.response import Response

class ExchangeRateView(APIView):
    
    serializer_class = ExchangeRateSerializer

    def get(self, request):
        query_set = ExchangeRate.objects.order_by('updated_at').last()
        serializer = ExchangeRateSerializer(query_set)
        return Response(serializer.data)
    
    def post(self, request):
        query_set = fetch_rate()
        serializer = ExchangeRateSerializer(query_set)
        return Response(serializer.data)
